# DOC-LAB-8-HOSTING-STATIC-WEBSITE
# Step 1: Clone GitHub Repository

```bash
git clone https://github.com/alfi-teachs/DOC-LAB-8-HOSTING-STATIC-WEBSITE.git
```
# Step 2: Go Inside Project Folder
```bash
cd DOC-LAB-8-HOSTING-STATIC-WEBSITE
```
# Step 3: Build Docker Image
```bash
docker build -t gym .
```
# Step 4: Run Docker Container
```bash
docker run -d -p 2000:80 --name gym-container gym
```
# Step 5: Check Running Containers 
```bash
docker ps
```
# Step 6: Open Website
```bash
http://localhost:2000
```
# Optional Commands

Stop Container
```bash
docker stop gym-container
```
Start Container Again
```bash
docker start gym-container
```
Remove Container
```bash
docker rm -f gym-container
```
Check Logs
```bash
docker logs gym-container
```
