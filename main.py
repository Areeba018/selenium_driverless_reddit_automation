import asyncio
import random
import json
import os
from typing import Any, Dict
import pyautogui

from selenium_driverless import webdriver

from reddit import reddit_login



TASK_STATUS_FILE = "task_status.json"

# Random sleep function
async def random_sleep(min_seconds=10, max_seconds=15):
    await asyncio.sleep(random.uniform(min_seconds, max_seconds))

# # Define the actions as individual functions
# async def perform_mouse_movement(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Performing Mouse Movement...")
#     start_x, start_y = pyautogui.position()
#     print(f"Initial mouse position: ({start_x}, {start_y})")
#     end_x = start_x + random.randint(50, 150)
#     end_y = start_y - random.randint(50, 150)
#     try:
#         await human_like_mouse_move(driver, start_x, start_y, end_x, end_y)
#         await random_sleep()
#     except Exception as e:
#         print(f"Error during mouse movement: {e}")

# async def perform_search_and_close(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Performing Search and Close Dropdown...")
#     await search_and_close_dropdown(driver)
#     await random_sleep()

# async def perform_ticker_interaction(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Performing Ticker Interaction...")
#     tickers = ["DIA", "DIS", "BURU", "MSFT", "TSLA", "AMZN", "NFLX", "META", "NVDA", "JPM"]
#     await click_tabs_and_scroll(driver)
#     await random_sleep()
#     await search_random_ticker(driver, tickers)
#     await random_sleep()
#     await click_tabs_and_scroll(driver)
#     await random_sleep()

# async def perform_like_ticker_post(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Performing Like Ticker Post...")
#     tickers = ["DIA", "DIS", "BURU", "MSFT", "TSLA", "AMZN", "NFLX", "META", "NVDA", "JPM"]
#     await search_ticker_and_interact(driver, tickers)
#     await random_sleep()

# async def perform_watchlist_bot(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Performing Watchlist Bot Interaction...")
#     await interact_with_watchlist(driver)
#     await random_sleep()

# async def perform_add_watchlist(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Adding Ticker to Watchlist...")
#     await click_on_watchlist_icon(driver)
#     await random_sleep()

# async def perform_like(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Liking Random Posts...")
#     await like_random_posts(driver, scrolls=3, max_likes=2)
#     await random_sleep()

# async def perform_like_in_thread(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Liking Posts in Thread...")
#     await like_random_post_in_thread(driver, scrolls=3, max_like=1)
#     await random_sleep()

# async def perform_comment(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Commenting on Random Posts...")
#     await comment_random_post(driver, scrolls=3, max_comments=1)
#     await random_sleep()

# async def perform_comment_in_thread(driver):
#     await driver.get("https://stocktwits.com/stream/popular", wait_load=True, timeout=120)
#     print("Commenting in Thread...")
#     await comment_random_post_in_thread(driver, scrolls=2, max_comments=1)
#     await random_sleep()


# Load or initialize task status
def load_task_status():
    if os.path.exists(TASK_STATUS_FILE):
        with open(TASK_STATUS_FILE, "r") as file:
            return json.load(file)
    # Default: All tasks are pending
    return {func: "pending" for func in ALL_ACTIONS.keys()}

def save_task_status(task_status):
    with open(TASK_STATUS_FILE, "w") as file:
        json.dump(task_status, file, indent=4)

# Actions dictionary
ALL_ACTIONS = {
    # "perform_mouse_movement": perform_mouse_movement,
    # "perform_search_and_close": perform_search_and_close,
    # "perform_ticker_interaction": perform_ticker_interaction,
    # "perform_watchlist_bot": perform_watchlist_bot,
    # "perform_like": perform_like,
    # "perform_add_watchlist":  perform_add_watchlist,
    # "perform_like_in_thread": perform_like_in_thread,
    # "perform_comment":  perform_comment,
    # "perform_comment_in_thread":  perform_comment_in_thread,
}

# # Randomized action runner
# async def start_activity(proxy: str, user: Dict[str, Any]):
#     task_status = load_task_status()
#     pending_tasks = [task for task, status in task_status.items() if status == "pending"]
    
#     if not pending_tasks:
#         print("\nAll tasks completed! Resetting tasks...\n")
#         task_status = {task: "pending" for task in ALL_ACTIONS.keys()}
#         pending_tasks = list(task_status.keys())

#     # Shuffle pending tasks and pick a random subset (e.g., 3 tasks)
#     random.shuffle(pending_tasks)
#     tasks_to_run = pending_tasks[:3]

#     print(f"Tasks to execute this run: {tasks_to_run}")

#     options = webdriver.ChromeOptions()
#     driver = await webdriver.Chrome(options=options)

#     try:
#         await stocktwits_login(driver, user)
#         for task in tasks_to_run:
#             try:
#                 print(f"Executing: {task}")
#                 await ALL_ACTIONS[task](driver)
#                 task_status[task] = "done"  # Mark task as completed
#                 save_task_status(task_status)
#                 await random_sleep()
#             except Exception as e:
#                 print(f"Error in {task}: {e}")
#     finally:
#         print("Closing driver...")
#         await driver.quit()




# Track run count in a file
RUN_COUNT_FILE = "run_count.json"

# Function to load or initialize the run counter
def load_run_count():
    if os.path.exists(RUN_COUNT_FILE):
        with open(RUN_COUNT_FILE, "r") as file:
            return json.load(file)["count"]
    return 0

def save_run_count(count):
    with open(RUN_COUNT_FILE, "w") as file:
        json.dump({"count": count}, file, indent=4)

# Randomized action runner with alternating behavior
async def start_activity(proxy: str, user: Dict[str, Any]):
    task_status = load_task_status()
    run_count = load_run_count()
    run_count += 1  # Increment the run count
    save_run_count(run_count)

    # Alternate between running all tasks and a random subset
    if run_count % 2 == 0:
        print("\nEven run count detected. Running all tasks...\n")
        tasks_to_run = list(ALL_ACTIONS.keys())  # Run all tasks
        task_status = {task: "pending" for task in ALL_ACTIONS.keys()}  # Reset task statuses
    else:
        print("\nOdd run count detected. Running 3 random tasks...\n")
        pending_tasks = [task for task, status in task_status.items() if status == "pending"]

        if not pending_tasks:
            print("\nAll tasks completed! Resetting tasks...\n")
            task_status = {task: "pending" for task in ALL_ACTIONS.keys()}
            pending_tasks = list(task_status.keys())

        # Shuffle pending tasks and pick 3 random ones
        random.shuffle(pending_tasks)
        tasks_to_run = pending_tasks[:3]

    print(f"Tasks to execute this run: {tasks_to_run}")

    options = webdriver.ChromeOptions()
    driver = await webdriver.Chrome(options=options)

    try:
        await reddit_login(driver, user)
        for task in tasks_to_run:
            try:
                print(f"Executing: {task}")
                await ALL_ACTIONS[task](driver)
                task_status[task] = "done"  # Mark task as completed
                save_task_status(task_status)
                await random_sleep()
            except Exception as e:
                print(f"Error in {task}: {e}")
    finally:
        print("Closing driver...")
        await driver.quit()



# Main execution
async def main():
    users_file = "users.json"
    with open(users_file) as file:
        users = json.load(file)

    for user in users:
        print(f"\nStarting activity for user: {user['user']['reddit']['username']}")
        await start_activity(user['proxy'], user['user']['reddit'])

if __name__ == "__main__":
    asyncio.run(main())
