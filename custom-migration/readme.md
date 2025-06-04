Writing a custom migration in Django allows you to execute arbitrary Python code during the migration process—ideal when you need to:

- Backfill or transform data.

- Execute non-schema-changing database commands.

- Use custom logic that isn't supported by standard migration operations.