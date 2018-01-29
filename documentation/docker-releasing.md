# Releasing using docker

Different than in most docker tutorials , the docker compose file and the docker files are not in the root of the project,
but in a separate docker folder. In order to run the command you need to add folder options:

<pre>docker-compose -f docker-compose.yml --project-directory . up</pre>