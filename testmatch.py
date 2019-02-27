    # Use the "video_dice" intent handler
    utterance = phrase.lower().replace("video", "")
    utterance = utterance.replace("dice", "")
    url = search(utterance)
    handle_video_dice(url)
    print(url)
