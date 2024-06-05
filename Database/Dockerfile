# Install Linux OS (Debian) + mysql specific version (good for us, cause won't break in the future.)
FROM mysql:8

# Copy beautiful_vacation.sql into docker special folder named /docker-entrypoint-initdb.d which installs it.
COPY ./beautiful_vacation.sql /docker-entrypoint-initdb.d