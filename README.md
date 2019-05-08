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
* DATA_DIR (holds the database 'training.db', defaults to '.')
* LOG_DIR (holds the log file 'training.log', defaults to '.')
* NATIVE_USER (user name for native postgres, defaults to 'trainingApp')
* NATIVE_PORT (defaults to 5432)
* NATIVE_HOST (defaults to db001.gda-score.org)
* CLOAK_USER (user name for cloak postgres, defaults to 'training')
* CLOAK_PORT (defaults to 9432)
* CLOAK_HOST (defaults to attack.aircloak.com)

## Updating dependencies

When adding new dependencies add them to `devel-requirements.txt` and run `make deps`.
This will download the required dependencies in your local virtual environment and also
updated the `requirements.txt` file used when deploying the application

## To run

- Download dependencies using `make deps`
- If running locally
  - Make a copy of `.env-dev-sample` and save it as `.env-dev` and edit it to fit your setup
  - Start the app with `make start-local`
- If running elsewhere start the app with `make start` and supply the required environment variables

The app automatically restarts with any code changes. If new menu items were added, then go to `domain:port/populateCache` to add the new queries to the cache.
