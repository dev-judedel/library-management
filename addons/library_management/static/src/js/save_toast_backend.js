/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

const MODEL_NAME = "library.management";

const originalSetup = FormController.prototype.setup;
const originalSaveRecord = FormController.prototype.saveRecord;
const originalSave = FormController.prototype.save;
const originalOnClickSave = FormController.prototype.onClickSave;
const originalOnSaveButtonClicked = FormController.prototype.onSaveButtonClicked;

function getResModel(controller) {
    return (
        controller?.props?.resModel ||
        controller?.model?.root?.resModel ||
        controller?.model?.config?.resModel ||
        null
    );
}

function notifySuccess(controller, message) {
    const notification =
        controller?.env?.services?.notification || controller?.notification || null;

    if (notification && typeof notification.add === "function") {
        notification.add(message, { type: "success" });
        return true;
    }

    if (typeof controller?.displayNotification === "function") {
        controller.displayNotification({ type: "success", message });
        return true;
    }

    return false;
}

function isNewRecord(controller) {
    const root = controller?.model?.root;
    if (!root) {
        return null;
    }
    if (typeof root.isNew === "function") {
        return root.isNew();
    }
    if (typeof root.isNew === "boolean") {
        return root.isNew;
    }
    if (root.resId !== undefined && root.resId !== null) {
        return !root.resId;
    }
    return null;
}

async function withSaveToast(controller, action) {
    if (controller._librarySaveToastActive) {
        return action();
    }

    controller._librarySaveToastActive = true;
    const wasNew = isNewRecord(controller);

    try {
        const result = await action();
        const saved = result !== false;
        if (saved && getResModel(controller) === MODEL_NAME) {
            const isNew = wasNew === true;
            const message = isNew
                ? "Book created successfully."
                : "Book updated successfully.";
            notifySuccess(controller, message);
        }
        return result;
    } finally {
        controller._librarySaveToastActive = false;
    }
}

patch(
    FormController.prototype,
    {
        setup() {
            if (this._super) {
                this._super(...arguments);
            } else if (originalSetup) {
                originalSetup.apply(this, arguments);
            }
            this.notification = this.env?.services?.notification || null;
        },

        async saveRecord() {
            return withSaveToast(this, async () => {
                if (this._super) {
                    return this._super(...arguments);
                }
                if (originalSaveRecord) {
                    return originalSaveRecord.apply(this, arguments);
                }
                return undefined;
            });
        },

        async save() {
            return withSaveToast(this, async () => {
                if (this._super) {
                    return this._super(...arguments);
                }
                if (originalSave) {
                    return originalSave.apply(this, arguments);
                }
                return undefined;
            });
        },

        async onClickSave() {
            return withSaveToast(this, async () => {
                if (this._super) {
                    return this._super(...arguments);
                }
                if (originalOnClickSave) {
                    return originalOnClickSave.apply(this, arguments);
                }
                return undefined;
            });
        },

        async onSaveButtonClicked() {
            return withSaveToast(this, async () => {
                if (this._super) {
                    return this._super(...arguments);
                }
                if (originalOnSaveButtonClicked) {
                    return originalOnSaveButtonClicked.apply(this, arguments);
                }
                return undefined;
            });
        },
    },
    { name: "library_management_save_toast" }
);
