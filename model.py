import tensorflow as tf
from keras import Sequential
from keras.layers import TFSMLayer # As keras now only supports .h5 and .keras but takes many arguments
def load_Model():
    # model = tf.keras.models.load_model('../model/my_model_4')
    model = tf.keras.models.load_model("BI_RNN.keras")
    print(model.summary())
    return model

def predict(df):
    model = load_Model()
    comments = df['Comments'].to_list()
    # print(comments.shape())
    for comment in comments:
        input_tensor = tf.constant([[comment]])  # shape (1, 1) as expected

        # Try all likely keys: "inputs", "input_1", "input_4"
        pred_probs = tf.squeeze(model(inputs=input_tensor))  # try input_1= or inputs=
        pred = tf.argmax(pred_probs).numpy()

        # print(f"Prediction = {pred}, Probability : {pred_probs.numpy()}")
        labels = {'cancel_order': 0, 'change_order': 1, 'change_shipping_address': 2, 'check_cancellation_fee': 3, 'check_invoice': 4, 'check_payment_methods': 5, 'check_refund_policy': 6, 'complaint': 7, 'contact_customer_service': 8, 'contact_human_agent': 9, 'create_account': 10, 'delete_account': 11, 'delivery_options': 12, 'delivery_period': 13, 'edit_account': 14, 'get_invoice': 15, 'get_refund': 16, 'newsletter_subscription': 17, 'payment_issue': 18, 'place_order': 19, 'recover_password': 20, 'registration_problems': 21, 'review': 22, 'set_up_shipping_address': 23, 'switch_account': 24, 'track_order': 25, 'track_refund': 26}
        print(f"Prediction = {[key for key, value in labels.items() if value == pred]}")
        # print(f"Prediction = {pred}")
        print(f"Comment : {comment}")

