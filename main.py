from src.agent.orchestrator import run_agent


def banner():
    print("\n" + "=" * 60)
    print("            SUPROC AI AGENT")
    print("=" * 60)


def main():
    banner()

    request = input("\nEnter Requirement:\n> ")

    print("\nSearching...\n")

    run_agent(request)


if __name__ == "__main__":
    main()