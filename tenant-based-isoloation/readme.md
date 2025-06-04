### Step 1: Define Your Tenant and User Models

In settings.py: 
`AUTH_USER_MODEL = 'yourapp.User'`

### Step 2: Create a Tenant-Aware Base Model

### Step 3: Create Your Business Model (e.g., Invoice)

### Step 4: Create Serializers

### Step 5: Create Views with Tenant Filtering

### Step 6: Register URL Patterns

### Step 7: Test the API

Using curl, Postman, or frontend:

- Only invoices belonging to the authenticated user’s - tenant are visible.
- When creating a new invoice, it automatically assigns the user’s tenant.