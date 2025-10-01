#!/bin/bash

# Function to update script and rebuild Docker container
update_and_rebuild() {
    echo "=== Updating Script and Rebuilding Docker Container ==="
    
    # Check if we're in the correct directory
    if [ ! -f "build.sh" ]; then
        echo "Error: build.sh not found. Please run this from the tfsites.common_docker directory."
        exit 1
    fi
    
    # Check if the combined script exists
    SCRIPT_PATH="tfsites-webportal/03-visualizeTfSitesOnSequences/03-combined-generateMotifDatabase-and-visualizeTfSitesOnSequences.py"
    if [ ! -f "$SCRIPT_PATH" ]; then
        echo "Error: Combined script not found at $SCRIPT_PATH"
        exit 1
    fi
    
    echo "✓ Script updated: $SCRIPT_PATH"
    echo "✓ Starting Docker build and push process..."
    
    # Run the build script
    chmod +x build.sh
    ./build.sh
    
    if [ $? -eq 0 ]; then
        echo "✓ Docker container successfully built and pushed!"
        echo "✓ New container available as: genepattern/tfsites:17.0"
    else
        echo "✗ Docker build failed!"
        exit 1
    fi
}

# If script is called directly, run the function
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    update_and_rebuild
fi
