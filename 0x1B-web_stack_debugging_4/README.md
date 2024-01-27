erver Optimization with Puppet

## Overview
This project aims to optimize the configuration of a web server (Nginx) using Puppet manifests. The goal is to improve the server's performance and ensure it can handle a specified load of requests without any failures.

## Requirements
- Ubuntu 14.04 LTS
- Puppet v3.4
- Nginx 1.4.6

## Usage
1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Apply the Puppet manifest to optimize the Nginx configuration:

    ```bash
    sudo puppet apply 0-the_sky_is_the_limit_not.pp
    ```

4. Restart the Nginx service to apply the new configuration:

    ```bash
    sudo service nginx restart
    ```

5. Run benchmark tests using ApacheBench to ensure the server can handle the specified load without any failed requests:

    ```bash
    ab -c 100 -n 2000 localhost/
    ```

## License
This project is licensed under the [MIT License](LICENSE).
