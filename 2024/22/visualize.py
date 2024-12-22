from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.init import init
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import hashlib

MOD = 16777216


def calculate(secret, iterations=1):
    for _ in range(iterations):
        mixed = (secret ^ (secret * 64)) % MOD
        div = ((mixed // 32) ^ mixed) % MOD
        secret = ((div * 2048) ^ div) % MOD
    return secret


def first_sequence_values(secret):
    seqs = {}
    last = ()
    prev = secret % 10

    for _ in range(2000):
        secret = calculate(secret)
        val = secret % 10
        last = (*last[-3:], val - prev)
        seqs.setdefault(last, val)
        prev = val
    return seqs


def calculate_best_sequence_dynamic(arr):
    totals = defaultdict(int)
    all_snapshots = []

    for secret in arr:
        seqs = first_sequence_values(secret)
        for k, v in seqs.items():
            totals[k] += v

        # Take a snapshot of the top 10 sequences
        top_10 = sorted(totals.items(), key=lambda item: item[1], reverse=True)[:10]
        all_snapshots.append(top_10)

    return all_snapshots


def get_sequence_color(sequence):
    """Generate a consistent color for each sequence using its hash"""
    # Use the hash of the sequence as a seed to generate a color
    hash_value = int(hashlib.md5(str(sequence).encode()).hexdigest(), 16)
    return plt.cm.viridis(hash_value % 256 / 255)  # Using the 'viridis' colormap


def visualize(arr, output_file="animation.gif"):
    # Get the snapshots of the top 10 sequences
    snapshots = calculate_best_sequence_dynamic(arr)

    # Initialize the figure and bar graph
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        in_pause = frame >= len(snapshots)

        if in_pause:
            top_10 = snapshots[-1]
        else:
            top_10 = snapshots[frame]
        sequences = [",".join(map(str, k)) for k, v in top_10]
        values = [v for k, v in top_10]

        colors = [get_sequence_color(seq) for seq in sequences]

        # Create the bar graph
        bars = ax.bar(sequences, values, color=colors)

        # Add values on top of the bars
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                str(value),
                ha="center",
                va="bottom",
                fontsize=10,
            )

        # Add sequence labels inside the bars (sideways)
        for bar, sequence in zip(bars, sequences):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() / 2,
                sequence,
                ha="center",
                va="center",
                rotation=90,
                color="white",
                fontsize=8,
                alpha=0.9,
            )

        ax.set(xticklabels=[])
        # Set axis labels and title
        ax.set_ylabel("Value")
        ax.set_xlabel("Sequences")
        if in_pause:
            ax.set(title="Final Top Sequences")
        else:
            ax.set(title=f"Top 10 Sequences After {frame + 1}/{len(snapshots)} Secrets")
        ax.set_ylim(0, max(max(values), 1) * 1.1)  # Dynamically scale y-axis

    # Create animation with extra frames for the pause at the end
    fps = 25
    interval = 1000 // fps
    pause_duration = 4  # seconds
    pause_frames = fps * pause_duration

    total_frames = len(snapshots) + pause_frames  # Add 10 frames for a 3-second pause
    ani = FuncAnimation(
        fig, update, frames=total_frames, interval=interval, repeat=False
    )

    if output_file.endswith(".gif"):
        ani.save(output_file, writer=PillowWriter(fps=fps))  # Save as GIF
    elif output_file.endswith(".mp4"):
        ani.save(output_file, writer="ffmpeg", fps=fps)  # Save as MP4
    plt.close(fig)


def main(args=None):
    arr = init(path.dirname(__file__), inputs.read_to_int_arr, args)
    visualize(arr)


if __name__ == "__main__":
    main(argv[1:])
