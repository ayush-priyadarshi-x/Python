def get_status_message(status: str) -> str:
    match status:
        case "active":
            return "User is active."
        case "inactive":
            return "User is inactive."
        case "suspended":
            return "User is suspended."
        case "banned":
            return "User is banned."
        case _:
            return "Unknown status."

# Test cases
print(get_status_message("active"))      # Output: User is active.
print(get_status_message("banned"))     # Output: User is banned.
print(get_status_message("unknown"))    # Output: Unknown status.
