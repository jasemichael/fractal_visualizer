import Gradient

def makeGradient(gradientName='BlackWhite'):
    if gradientName == "BlackWhite":
        return Gradient.BlackWhite
    elif gradientName == "BlueGreen":
        return Gradient.BlueGreen
    elif gradientName == "RedYellow":
        return Gradient.RedYellow
    else:
        raise NotImplementedError("Invalid gradient requested")