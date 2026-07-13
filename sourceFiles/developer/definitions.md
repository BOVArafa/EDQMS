This document must be used as a prompt to create a plan for the prototype redesign.
All UI (html or css) elements mentioned in this document will have `#` symbol as prefix.

# Modules

Modules represent the `#buttons` on the `#sidebar`, representing a row of `#tabs` (tables).

# Tables

Every `#screenLabel` is composed by tree main sessions: a `#tab` row with all the tables in the module, the table with all data for the selected tab (entity) and a `#report` session.

The table exists so the user can have a look in every record for the given entity.

# Reports

Every `#tab` has a session for reports that should use data from the entity table relative to the tab.

# Filers

Each report can have one or more filter to help users understand the data being displayed on the table.

