/** @odoo-module **/

const TARGET_LENGTH = 13;
const FIELD_SELECTOR = ".o_isbn_counter_target";
const COUNTER_CLASS = "o_isbn_counter";
const ATTACHED_ATTR = "data-isbn-counter-attached";

function updateCounter(input, counter) {
    const value = input.value || "";
    counter.textContent = `${value.length}/${TARGET_LENGTH}`;
}

function attachCounter(fieldWidget) {
    if (!fieldWidget || fieldWidget.getAttribute(ATTACHED_ATTR) === "1") {
        return;
    }

    const input = fieldWidget.querySelector("input");
    if (!input) {
        return;
    }

    const counter = document.createElement("div");
    counter.className = `text-muted ${COUNTER_CLASS}`;
    counter.setAttribute("aria-live", "polite");

    const onInput = () => updateCounter(input, counter);
    input.addEventListener("input", onInput);
    input.addEventListener("change", onInput);

    updateCounter(input, counter);

    if (input.parentElement) {
        input.parentElement.appendChild(counter);
    } else {
        fieldWidget.appendChild(counter);
    }

    fieldWidget.setAttribute(ATTACHED_ATTR, "1");
}

function scan(root) {
    const scope = root || document;
    const fields = scope.querySelectorAll(FIELD_SELECTOR);
    fields.forEach(attachCounter);
}

function init() {
    scan(document);

    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType !== Node.ELEMENT_NODE) {
                    return;
                }
                if (node.matches && node.matches(FIELD_SELECTOR)) {
                    attachCounter(node);
                } else if (node.querySelector) {
                    scan(node);
                }
            });
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}
