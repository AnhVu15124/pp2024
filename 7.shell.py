import os
import subprocess

def running_program(command):
    try:
        args = command.split()
        if "<" in args:
            index = args.index("<")
            input_file =  args[index+1]
            args = args[:index]
        else:
            input_file = None
        if ">" in args:
            index = args.index(">")
            output_file =  args[index+1]
            args = args[:index]
        else:
            output_file = None
        if input_file:
            with open(input_file, 'r') as f:
                result = subprocess.run(args, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else: 
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if output_file:
            with open(output_file, 'w') as f:
                f.write(result.stdout.decode())
        else:
            print(result.stdout.decode())

        if result.returncode != 0:
            print("Error: ", result.stdout.decode())

    except Exception as e:
        print("Error: ", str(e))

def main():
    while True:
        command = input("Command: ")
        if command.lower() == 'exit':
            break
        else:
            running_program(command)

if __name__ == "__main__":
    main()