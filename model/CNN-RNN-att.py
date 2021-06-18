from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Reshape
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import LSTM, Bidirectional
from keras.utils import np_utils
from keras import optimizers
from keras_self_attention import SeqSelfAttention
from keras.layers import Flatten


filters = 250
kernel_size = 9
pool_size = 4
lstm_output_size = 16

print('Building model...')
model = Sequential()
model.add(Reshape((1000,20),input_shape=(20000,)))
model.add(Conv1D(filters,kernel_size,padding = 'valid',activation = 'relu',strides = 1))
model.add(MaxPooling1D(pool_size = pool_size))
model.add(Bidirectional(LSTM(lstm_output_size, return_sequences=True,activation = 'tanh')))
print(model.outputs)
model.add(SeqSelfAttention(attention_activation='sigmoid'))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

custom_objects = SeqSelfAttention.get_custom_objects()


