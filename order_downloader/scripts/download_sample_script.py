import subprocess, os


def run_download_sample_routine(order):
    dist_path = "/dist"
    pipelines_path = "/nextflow-pipelines"
    log_path = "/var/log/nextflow"
    env = dict(os.environ, DIST_PATH=dist_path, PIPELINES_PATH=pipelines_path, LOG_PATH=log_path)
    p1 = subprocess.Popen(f"sshpass -p '$params.PASS' scp -oHostKeyAlgorithms=+ssh-rsa -oHostKeyAlgorithms=+ssh-dss \
    -oPubkeyAcceptedAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-dss -oStrictHostKeyChecking=no \
    -r $params.USER@$params.HOST:$params.SRC_PATH/{order} INCOMING".split(" "),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    stdout, stderr = p1.communicate()
    return stdout.decode('ascii').replace("\n", "")
