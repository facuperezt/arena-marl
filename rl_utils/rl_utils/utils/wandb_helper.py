import wandb


class WandbLogger:
    def __init__(self, project_name):
        self.project_name = project_name
        wandb.init(project=project_name)

    def update_hyperparameters(self, hyper_params, robot_params, robot):
        for key, value in hyper_params.items():
            wandb.config[f"{robot}/{key}"] = value
        for key, value in robot_params.items():
            wandb.config[f"{robot}/{key}"] = value

    def log(self, title: str, dict_to_log: dict, step: int):
        """Create log entry for ``title``.

        Args:
            title (str): title of the log entry/ chart
            dict_to_log (dict): the dictionary that is to be logged. \
                Hereby the format has to be: \
                ``{robot1: value1, robot2: value2, ...}``
            step (int): the step of updating the respective metric
        """
        formatted_dict = {
            f"{title}/{robot}": value for robot, value in dict_to_log.items()
        }
        wandb.log(formatted_dict, step=int(step))  # , commit=True)

    def log_single(self, title: str, value: int, step: int):
        """Create log entry for ``title``.

        Args:
            title (str): title of the log entry/ chart
            value (int): the value that is to be logged for step ``step``
            step (int): the step of updating the respective metric
        """
        # wandb.log({title: value}, step=int(step), commit=True)
        wandb.log({title: value}, step=int(step))  # , commit=True)
