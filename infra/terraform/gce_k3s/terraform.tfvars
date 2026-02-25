project_id = "project-8d8e946e-d1b3-4114-8ed"
region     = "us-central1"
zone       = "us-central1-a"

instance_name     = "edu-k3s-vm"
machine_type      = "e2-medium"
boot_disk_size_gb = 30
ssh_user          = "hoda067"
ssh_public_key    = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFVddjDkOaUVX09cfH1HzeL5S2Zm0TvSX13jKnRj89yT hoda067"

allow_http_cidrs = ["0.0.0.0/0"]

labels = {
  owner = "devops-class"
  stage = "training"
}