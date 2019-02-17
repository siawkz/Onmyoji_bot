# Onmyoji_bot
Onmyoji Traditional Chinese Edition Automation Script

Consists of two python scripts:
1. autoStage.py
    To start stage level 28 clear with or without friend automatically.

    You have to invite friend manually for the very first time.
    ```python
    auto_stage(is_team=False, continue_half=False) # is_team: Start automation with friend, continue_half: continue half way stage clear 
    ```
2. autoJoinStage.py
    To join stage automatically
    ```python
    auto_join_stage(continue_half=False) #continue_half: continue half way stage clear 
    ```