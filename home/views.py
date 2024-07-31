from django.shortcuts import render, HttpResponse
from subprocess import run
import os
from django.views.decorators.csrf import csrf_exempt
import random
import requests
import string
from datetime import datetime, timedelta

# def generate_random_path(length=8):
#     """Generate a random path."""
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for _ in range(length))

# def generate_unique_paths(num_paths, length=8):
#     """Generate a list of unique random paths."""
#     paths = set()
#     while len(paths) < num_paths:
#         path = generate_random_path(length)
#         paths.add(path)
#     return list(paths)

# Example usage:

# num_paths = 10  # Number of unique paths needed
# paths = generate_unique_paths(num_paths)
# serialNum = [str(num) for num in range(100, 201)]
# @csrf_exempt
# def start_vm(request):
#     port = ports.pop(0)
#     path = paths.pop(0)
#     num = serialNum.pop(0)
#     if request.method == 'POST':
#         command = [
#             'docker', 'run', '-d',
#             '--hostname', 'kalilinux.lab',
#             '--restart', 'always',
#             '--cap-add', 'NET_ADMIN',
#             '-p', f'{port}:8080',
#             '-e', 'SHELL=/bin/bash',
#             '-e', 'PASSWORD=kalilinux',
#             '--label', 'traefik.enable=true',
#             '--label', f'traefik.http.routers.kalilinux{num}.rule=Host(`kalilinux{num}`) && PathPrefix(`/{path}/`)',
#             '--label', f'traefik.http.services.kalilinux{num}.loadbalancer.healthcheck.hostname=localhost',
#             '--label', f'traefik.http.services.kalilinux{num}.loadbalancer.server.scheme=http',
#             '--label', f'traefik.http.services.kalilinux{num}.loadbalancer.server.port=8080',
#             '--name', f'kalilinux{num}',
#             'csalab/kalilinux-docker:latest'
#         ]
#         run(command)
#         # Assuming you don't need to capture output
#         vm_url = f"http://127.0.0.1/{path}/vnc.html"
#         return render(request, 'index.html', {'vm_url': vm_url, 'message': 'Virtual machine started!'})
#     else:
#         return render(request, 'index.html')
        

serialNum = [str(num) for num in range(100, 201)]
used_ports = []
ports = [str(port) for port in range(8001, 8901)]

@csrf_exempt
def start_vm(request):
    port = ports.pop(0)
    num = serialNum.pop(0)
    if num == 201:
        serialNum = serialNum = [str(num) for num in range(100, 201)]
    if port == 8900:
        ports = [str(port) for port in range(8001, 8101)]

    if request.method == 'POST':
        expiration_time = (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        command = [
            'docker', 'run', '-d',
            '--hostname', 'kalilinux.lab',
            '--restart', 'always',
            '--cap-add', 'NET_ADMIN',
            '-p', f'{port}:8080',
            '-e', 'SHELL=/bin/bash',
            '-e', f'PASSWORD=kalilinux',
            '--label', f'expiration={expiration_time}',
            '--name', f'kalilinux{num}',
            'csalab/kalilinux-docker:latest'
        ]
        run(command)
        # Assuming you don't need to capture output
        vm_url = f"http://13.126.89.59 :{port}/vnc.html"
        return render(request, 'index.html', {'vm_url': vm_url, 'message': 'Virtual machine started!'})
    else:
        return render(request, 'index.html')

from django.http import JsonResponse

serialNum = [str(num) for num in range(100, 201)]
used_ports = []
ports = [str(port) for port in range(8001, 8901)]

@csrf_exempt
def start_vm(request):
    global ports, serialNum
    port = ports.pop(0)
    num = serialNum.pop(0)
    if num == 201:
        serialNum = serialNum = [str(num) for num in range(100, 201)]
    if port == 8900:
        ports = [str(port) for port in range(8001, 8101)]

    if request.method == 'POST':
        expiration_time = (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        command = [
            'docker', 'run', '-d',
            '--hostname', 'kalilinux.lab',
            '--restart', 'always',
            '--cap-add', 'NET_ADMIN',
            '-p', f'{port}:8080',
            '-e', 'SHELL=/bin/bash',
            '-e', f'PASSWORD=kalilinux',
            '--label', f'expiration={expiration_time}',
            '--name', f'kalilinux{num}',
            'csalab/kalilinux-docker:latest@sha256:8547cae174e2a62cf20d33bea57ce58e5a7f62a8f33884b8351877f7baccce69'
        ]
        run(command)
        # Assuming you don't need to capture output
        vm_url = f"http://3.109.29.160:{port}/vnc.html"
        return render(request, 'index.html', {'vm_url': vm_url, 'message': 'Virtual machine started!'})
    else:
        return render(request, 'index.html')

@csrf_exempt
def req_vm(request):
    global ports, serialNum
    port = ports.pop(0)
    num = serialNum.pop(0)
    if num == 201:
        serialNum = serialNum = [str(num) for num in range(100, 201)]
    if port == 8900:
        ports = [str(port) for port in range(8001, 8101)]

    if request.method == 'POST':
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        expiration_time = (datetime.utcnow() + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        command = [
            'docker', 'run', '-d',
            '--hostname', 'kalilinux.lab',
            '--restart', 'always',
            '--cap-add', 'NET_ADMIN',
            '-p', f'{port}:8080',
            '-e', 'SHELL=/bin/bash',
            '-e', f'PASSWORD={password}',
            '--label', f'expiration={expiration_time}',
            '--name', f'kalilinux{num}',
            'csalab/kalilinux-docker:latest@sha256:8547cae174e2a62cf20d33bea57ce58e5a7f62a8f33884b8351877f7baccce69'
        ]
        run(command)
        vm_url = f"http://3.109.29.160:{port}/vnc.html"
        response_data = {
            'message': 'Virtual machine requested!',
            'vm_url': vm_url,
            'password': password
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def index(request):
    return render(request, 'index.html',)


def show_vm(request):
    return render(request, 'show_vm.html',context={'url':'http://3.109.29.160:8007/vnc.html'})


