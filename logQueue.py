import queue

#create a queue to hold log messages
log_queue = queue.Queue()

#link queue to TextHandler
text_handler = TextHandler(gui.log_window, log_queue)
text_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
text_handler.setLevel(logging.INFO)

#link queue to logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(text_handler)

#start the queue listener
queue_listener = logging.handlers.QueueListener(log_queue, text_handler)
queue_listener.start()
