# TargetPractice/interface/manager.py
from interface import title_page, loading_page

def run_sequences():
    """Runs the streamlined introduction sequences using your new descriptive file names."""
    # 1. Shows your unified split-screen instructions layout
    title_page.show_tutorial()
    
    # 2. Launches your newly renamed loading transition card
    loading_page.show_ready_screen()
