from transformers import Wav2Vec2Config, Wav2Vec2Model
# the implementation comes from: https://huggingface.co/docs/transformers/model_doc/wav2vec2
# the original paper can be found here: https://arxiv.org/abs/2006.11477

# initialize a standard configuration
# an own configuration can be created too
configuration = Wav2Vec2Config()

# initialize a model with random weights
model = Wav2Vec2Model(configuration)

# access the model configuration
configuration = model.config
