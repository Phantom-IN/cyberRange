#!/bin/bash

# Get list of running containers
containers=$(docker ps --format "{{.ID}}:{{.Names}}")

# Current timestamp
current_time=$(date +%s)

# Loop through each container
while IFS= read -r container; do
    container_id=$(echo "$container" | cut -d ':' -f 1)
    container_name=$(echo "$container" | cut -d ':' -f 2)
    
    # Get container uptime
    start_time=$(docker inspect --format='{{.State.StartedAt}}' "$container_id")
    start_timestamp=$(date -d "$start_time" +%s)
    uptime=$((current_time - start_timestamp))
    
    # Check if uptime is greater than 1 hour (3600 seconds)
    if [ $uptime -gt 3600 ]; then
        echo "Removing container $container_name (ID: $container_id)..."
        docker stop "$container_id" >/dev/null 2>&1
        docker rm "$container_id" >/dev/null 2>&1
    fi
done <<< "$containers"