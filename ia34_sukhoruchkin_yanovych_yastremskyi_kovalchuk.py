import os
from loguru import logger
import sys

min_level = "INFO"

def min_level_filter(record):
    return record["level"].no >= logger.level(min_level).no

logger.remove()
logger.add(sys.stderr, format="[{time:HH:mm:ss.SSS} | <level>{level: <8}</level>] {message}", filter=min_level_filter)

def knapsack(W, n, items):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        vi, wi = items[i - 1]
        for w in range(W + 1):
            if wi > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)
    return dp[n][W]

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        W, n = map(int, lines[0].split())
        items = [tuple(map(int, line.split())) for line in lines[1:]]
    return W, n, items

def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result) + '\n')

directory = os.getcwd() + "\\input"

for input_file in os.listdir(directory):
    if input_file.startswith('input'):
        logger.info(f"{input_file} - Starting to work with the file")
        W, n, items = read_input(os.getcwd() + "\\input\\" + input_file)
        logger.debug(f"{input_file} - Read the file")
        result = knapsack(W, n, items)
        logger.debug(f"{input_file} - Ran the algorithm")
        output_name = os.getcwd() + "\\output\\" + input_file.replace('input', 'output')
        write_output(output_name, result)
        logger.info(f"{input_file} - Wrote to file {output_name}")