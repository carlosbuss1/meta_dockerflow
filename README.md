### **Step 5: Run Workflow as a Test

- To confirm everything works, you can clone the repository elsewhere and test it:

git clone https://github.com/carlosbuss1/meta_dockerflow.git
cd meta_dockerflow
docker build -t taxonomic_analysis .
docker run --name taxo_output taxonomic_analysis
docker cp taxo_output:/app/output ./output
docker rm taxo_output
