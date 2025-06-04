## What is a Custom Model Manager?

A model manager is a Django class that provides database query operations for a model.

By default, Django adds a manager called .objects to every model.

A custom manager is a subclass of models.Manager where you can add your own query methods.

<br>

## Why Use Custom Model Manager? (The Need)

### 1. Encapsulate Common Query Logic
- If you often filter the same way (e.g., active users, published posts), put it in one place.
- Avoid repeating .filter(is_active=True) all over your code.

### 2. Improve Code Readability & Maintainability
- Cleaner, self-documenting code like Product.active() instead of repeating filters everywhere.
- Makes your business rules explicit and reusable.

### 3. Add Custom Query Methods
- Example: .expensive(), .recent(), .for_tenant(tenant).
- Allows chaining for expressive queries: Product.active().expensive()

### 4. Separate Concerns
- Keeps database query logic inside models.
- Views, forms, and serializers don’t have to know the filtering details.

### 5. Override Default QuerySet Behavior
- You can change the default queryset, e.g., to hide soft-deleted records by default.

<br>

## Example Use Cases

- Soft delete filtering: Only return records where `is_deleted=False`
- Multitenancy: Filter records by current user’s tenant/organization
- Status filtering: Return only published posts, active accounts, etc.
- Custom complex queries: Annotate, aggregate, or join with other tables


<br>

## Summary: Why Custom Managers?

| Benefit                       | Description                              |
| ----------------------------- | ---------------------------------------- |
| **Reusability**               | Write once, use everywhere               |
| **Clarity**                   | Meaningful method names like `.active()` |
| **Centralized logic**         | Easy to update filtering/business rules  |
| **Extendability**             | Add new querying methods easily          |
| **Cleaner views/controllers** | Less clutter in views, focus on logic    |
