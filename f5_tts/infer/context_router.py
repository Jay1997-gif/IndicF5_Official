from .context_analyzer import analyze


def route_by_context(token):

    token_type = analyze(token)

    return {
        "token": token,
        "type": token_type,
    }