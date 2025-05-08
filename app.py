def main():
    print("Hello from DevOps Demo!")
    with open("output.txt", "w") as file:
        file.write("Deployment successful!")

if __name__ == "__main__":
    main()