import subprocess
import git
import yaml
# examples
#git.Git("aa").clone("https://bitbucket.org/corebiz_ag/admin_animale.git")
#git("clone", "https://bitbucket.org/corebiz_ag/microservices-admin.git")

with open(r'./proton.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

print(fruits_list)