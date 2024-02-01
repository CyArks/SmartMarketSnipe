from ImageAnalysisTool import analyze_image
from MarketComparisonTool import get_average_market_price


def analyze_condition(offer):
    # For example, using image analysis to determine product condition
    condition_score = 0
    for image_url in offer.imageUrls:
        condition_score += analyze_image(image_url)
    # Normalize or adjust the condition score as needed
    return condition_score


def calculate_potential_gain(offer):
    # Analyze the product's condition from the description or images
    condition_score = analyze_condition(offer)

    # Estimate market price
    average_market_price = get_average_market_price(offer.title, condition_score)

    # Calculate potential gain
    potential_gain = average_market_price - offer.price
    return potential_gain
