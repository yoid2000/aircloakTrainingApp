# aircloakTrainingApp
App used to help users learn the Aircloak system.

The app is based on the bottle web framework.

## To configure

### Example menu items
Add menu items to demoConfig.py.

### Environment Variables

### Mandatory
* NATIVE_PASS (password for native postgres, no default)
* CLOAK_PASS (password for cloak postgres, no default)

### Optional
* PORT (defaults to 8080)
* DATA_DIR (holds the database 'training.db', defaults to .)
* LOG_DIR (holds the log file 'training.log', defaults to .)
* NATIVE_USER (user name for native postgres, defaults to 'trainingApp'
* NATIVE_PORT (defaults to 5432)
* NATIVE_HOST (defaults to db001.gda-score.org)
* CLOAK_USER (user name for cloak postgres, defaults to 'training'
* CLOAK_PORT (defaults to 9432)
* CLOAK_HOST (defaults to attack.aircloak.com)

## To run
The app automatically restarts with any code changes. If new menu items were added, then go to `domain:port/populateCache` to add the new queries to the cache.
