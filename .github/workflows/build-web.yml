name: Build and Deploy EasyList Website

on:
  push:
    branches:
      - content

permissions:
  contents: write

jobs:
  build-and-deploy:
    if: github.repository == 'easylist/easylist.github.io'
    runs-on: ubuntu-latest
    
    steps:
    - name: Security Check
      run: |
        echo "✅ Repository: ${{ github.repository }}"
        echo "✅ Actor: ${{ github.actor }}"
        if [ "${{ github.repository_owner }}" != "easylist" ]; then
          echo "❌ Unauthorized repository owner: ${{ github.repository_owner }}"
          exit 1
        fi
        
    - name: Checkout repository
      uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    
    - name: Install dependencies
      run: |
        pip install pelican
    
    - name: Configure Git
      run: |
        git config --global user.email "github-actions@github.com"
        git config --global user.name "GitHub Actions"
        git config --global push.default "matching"
    
    - name: Clone output repository
      run: |
        echo "Attempting to clone with token authentication..."
        git clone -b master "https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/easylist/easylist.github.io" output
    
    - name: Generate website
      run: |
        pelican -s publishconf.py -o output content
    
    - name: Commit and push changes
      run: |
        cd output
        git add --all .
        git commit -m "Publishing content revision $(git --git-dir ../.git rev-parse --short HEAD)"
        git push --force origin master:master
