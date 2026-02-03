# Library App - Renamed Module

## Changes Made

All references changed from `library_management` to `library_app`:

### Files Changed:
1. **Folder name**: `library_management/` → `library_app/`
2. **Model file**: `library_management.py` → `library_app.py`
3. **Model name**: `library.management` → `library.app`
4. **View files**: Renamed to `library_app_views.xml` and `library_app_menus.xml`
5. **Access rights**: Updated to `model_library_app`
6. **Controller**: Updated model reference to `library.app`

## Installation Steps

### Step 1: Backup & Remove Old Module
```bash
# 1. Uninstall the old module in Odoo (Apps menu)
# 2. Delete the old folder
rm -rf C:\odoo18-projects\library-project\addons\library_management
```

### Step 2: Copy New Module
```bash
# Copy the library_app folder to your addons directory
# Place it at: C:\odoo18-projects\library-project\addons\library_app\
```

### Step 3: Restart Odoo
```bash
# Restart your Odoo service/container
docker-compose restart  # or your restart method
```

### Step 4: Update Apps List
1. Go to Odoo → Apps
2. Click "Update Apps List"
3. Search for "Library Management"
4. Install the module

### Step 5: Verify
- Check that technical name shows as `library_app`
- Test CRUD operations
- Visit: http://localhost:8069/library/books

## File Structure

```
library_app/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   └── library_app.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── library_app_views.xml
│   ├── library_app_menus.xml
│   └── library_books_template.xml
└── static/
    └── description/
        └── icon.png (copy from old module)
```

## Important Notes

- Don't forget to copy the `icon.png` file from your old module
- All data from old module will be lost (create new records)
- The technical name is now `library_app`
- The model name is `library.app`

## Testing Checklist

- [ ] Module installs successfully
- [ ] Can create new book records
- [ ] Can edit existing books
- [ ] Can delete books
- [ ] ISBN validation works
- [ ] Active/Inactive filters work
- [ ] Website page displays books correctly
- [ ] Form layout (fields left, image right) works
- [ ] Tree view shows all columns
