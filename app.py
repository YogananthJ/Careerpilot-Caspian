from crewai_client import ask_careerpilot


def main():
    print("===================================")
    print("       CareerPilot AI")
    print("===================================")

    message = input("\nYou: ")

    print("\nCareerPilot is thinking...\n")

    try:
        response = ask_careerpilot(message)

        print("CareerPilot:")
        print(response)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()