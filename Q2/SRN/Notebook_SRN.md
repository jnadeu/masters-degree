**Briefing Document: Recurrent Neural Networks (RNNs), Convolutional Neural Networks (CNNs), LSTMs, GRUs, and Tokenization**

**I. Overview**

This document summarizes key concepts from lectures on Recurrent Neural Networks (RNNs), advanced Convolutional Neural Networks (CNNs), Long Short-Term Memory networks (LSTMs) and Gated Recurrent Units (GRUs), and tokenization techniques used in Natural Language Processing (NLP). The material covers the architectures, advantages, challenges, and applications of these neural network types, along with the fundamental process of preparing text data for these models.

**II. Recurrent Neural Networks (RNNs)**

- **Core Idea:** RNNs are designed for sequential data by maintaining a "memory" of past inputs. "RNNs are a class of neural networks that model sequential data by maintaining a 'memory' of past inputs." Outputs depend on both the current input and previous states.
- **Key Features:**
- **Weight Sharing:** "The weights in a recurrent layer are the same for every time step." This reduces the number of parameters and allows RNNs to process variable-length sequences. This is a "key feature of recurrent neural networks (RNNs) called weight sharing over time," similar to convolutions in CNNs.
- **Sequential Processing:** RNNs model time dependencies, capturing short-term and long-term dependencies.
- **Architecture:** RNNs can be many-to-one or many-to-many architectures. "An RNN takes many inputs and can return one, or several outputs: it is a many-to-one or many-to-many architecture."
- **Applications:** Natural Language Processing (NLP), time-series analysis, speech recognition, and video analysis. "Natural Language Processing (NLP): Sentiment analysis, machine translation, text generation. Time-Series Analysis: Weather prediction, stock forecasting."
- **Challenges:**
- **Sequential Processing Limits Parallelization:** This is a core limitation. "Sequential processing limits parallelization."
- **Vanishing/Exploding Gradients:** Due to the depth of the "unrolled" network, RNNs are prone to unstable gradients during backpropagation, particularly with long sequences. "In deep feedforward neural networks, backpropagation has unstable gradients because the product of many small gradients or of many big gradients can become very small or very big very quickly. This makes RNNs prone to exploding and vanishing gradients."
- **Backpropagation Through Time (BPTT):** RNNs are trained using BPTT, where each timestep of the unrolled network is treated as a layer. The aggregated gradient (sum of gradients at each timestep) is used for weight updates. A truncated version (TBPTT) is often used to mitigate vanishing/exploding gradients and speed up training.
- **Loss Functions:** Standard loss functions are used for classification and regression. Many-to-many architectures with variable length sequences require summing the loss over all time steps. Generative tasks need specific loss functions based on output probabilities.

**III. Convolutional Neural Networks (CNNs)**

- **Core Idea:** CNNs exploit spatial structure in data, particularly images.
- **Key Features:**
- **Convolutional Filters:** "The output for each pixel is a new value, a weighted sum of the pixel values in its local neighborhood." These filters are learnable weights that detect important features.
- **Pooling:** Downsampling operation that reduces parameters and computation, making the model invariant to small changes in input (rotations, translations). "After pooling, we have smaller images: this means a decrease in parameters and computation."
- **Spatial Structure:** "This takes advantage of the spatial structure, which we cannot do if we flatten the image to 1-D."
- **Backpropagation:** Similar to RNNs, filter weights are shared. The gradient for a filter is the sum of gradients from all positions where the filter was applied. Pooling layers affect gradient flow, but don't have learnable weights.
- **Key Architectures:**
- **LeNet:** Early CNN architecture using convolution and pooling.
- **AlexNet:** Deeper model demonstrating the importance of depth, ReLU activations, dropout, and GPU implementation.
- **VGG-Net:** Standardized layer design using small (3x3) filters to increase depth.
- **Inception:** Uses parallel networks (Inception modules) with convolutions of different sizes. Addresses the vanishing gradient problem with auxiliary classifiers.
- **ResNet:** Utilizes skip connections/residual blocks to pass input unaltered to later layers, enabling training of very deep networks.
- **Advanced Architectures:**
- **Sparsely connected architectures and parallel convolutions (Inception modules) allow us to use convolutions of different sizes."**
- **Skip connections "brute force” an identity layer" and avoid "degradation" caused by deep architectures.**
- **Depthwise Separable Convolutions:** Efficient architectures like MobileNet use depthwise separable convolutions to reduce computational cost. "MobileNet achieves efficiency by using depthwise separable convolutions"

**IV. LSTMs and GRUs**

- **Long-Term Dependencies:** Addressing the limitations of standard RNNs in capturing long-term dependencies due to vanishing/exploding gradients. "In practice, RNNs do not handle long term dependencies well: ‘gradient based learning algorithms face an increasingly difficult problem as the duration of the dependencies to be captured increases’."
- **LSTMs (Long Short-Term Memory Networks):**
- **Core Idea:** Add a "memory cell" to the RNN architecture to store and access information over long periods. "LSTMs take an input, the result of the previous layer and a memory cell to produce an output at each time step."
- **Gates:** Control the flow of information into and out of the memory cell:
- **Forget Gate:** Decides what information to discard. "Forget Gate: Decides what information should be thrown away or kept."
- **Input Gate:** Updates the cell state with new information. "Input Gate: Updates the cell state with new information."
- **Output Gate:** Determines the next hidden state. "Output Gate: Determines the next hidden state, influencing the output at the current timestep based on the cell state."
- **Memory Cell:** Updated minimally, preserving raw information and avoiding vanishing gradients. "The memory cell is updated without being passed through activation functions like tanh or sigmoid, preserving raw information."
- **Hidden State:** A processed version of the cell state used for computation. "The hidden state contains a processed version of the cell state that goes through the output gate and a tanh activation before being used in the next step."
- **GRUs (Gated Recurrent Units):**
- **Core Idea:** Simplification of LSTMs by using a single hidden state instead of a separate memory cell. "Why have a separate cell state when we can do everything through the hidden state?"
- **Gates:**
- **Reset Gate:** Determines how much of the previous hidden state to forget. "Reset gate: The reset gate determines how much of the previous hidden state to forget."
- **Update Gate:** Determines how much of the candidate activation vector to incorporate into the new hidden state. "Update gate: The update gate determines how much of the candidate activation vector to incorporate into the new hidden state."
- **Advantages:** Faster, easier to train (fewer parameters), performs similarly to LSTMs on many tasks.
- **Applications (LSTMs and GRUs):**
- NLP (Language modeling, machine translation, sentiment analysis)
- Time-series (Stock prices, weather)
- Speech and Audio (Speech-to-text, voice synthesis)
- **Challenges and Limitations:** Hyperparameter tuning can be tricky. Cannot handle very long sequences as effectively as Transformers.

**V. Tokenization**

- **Definition:** The process of breaking text into smaller units (tokens). "Breaking text into smaller units, i.e. tokens."
- **Key Concepts:**
- **Token:** An instance of a sequence of characters.
- **Type:** Class of all tokens containing the same character sequence.
- **Vocabulary:** Collection of all types.
- **Tokenization Methods:**
- **Character-based:** Splitting text into individual characters. Useful for languages where characters carry information, and it results in a small vocabulary. Disadvantage: Characters may not have meaning and create larger sequences.
- **Word-based:** Splitting text by spaces. Simple to implement but can lead to huge vocabulary sizes and issues with languages without spaces. "Splitting the text by spaces. Other delimiters such as punctuation can be used."
- **Challenges:** Dealing with contractions, compound words, and languages without spaces. Examples: San Francisco, German noun compounds, Chinese and Japanese texts.
- **Logits:** Un-normalized outputs before the activation function. "Un-normalized outputs, not passed through an activation function."


***

# Recurrent and Convolutional Neural Networks: A Deep Dive Study Guide

## Quiz

Answer the following questions in 2-3 sentences each.

1. What distinguishes Recurrent Neural Networks (RNNs) from feedforward networks and Convolutional Neural Networks (CNNs) in terms of the type of data they are designed to handle?
2. Explain the concept of "weight sharing over time" in RNNs and why it is a key feature.
3. Describe the purpose of the input gate in a Long Short-Term Memory (LSTM) network.
4. What is the role of pooling layers in CNNs, and how do they contribute to the network's performance?
5. Explain the issue of vanishing gradients in deep neural networks.
6. What are the advantages and disadvantages of character-based tokenization?
7. Explain what residual blocks do in ResNet CNN architecture.
8. Describe Truncated Backpropagation Through Time (Truncated BPTT) and why it is used.
9. What is the difference between tokens, types, and vocabulary in natural language processing? Give an example.
10. Explain the concept of depthwise separable convolutions and why they are used.

## Quiz Answer Key

1. RNNs are designed to handle sequential data, such as time series, speech, or text, by maintaining a "memory" of past inputs and modeling dependencies across time or sequence positions. Unlike feedforward networks and CNNs, RNNs can process variable-length inputs and outputs, making them suitable for tasks where the order of information matters.
2. "Weight sharing over time" in RNNs refers to the fact that the weights in a recurrent layer are the same for every time step in the sequence. This significantly reduces the number of parameters and allows the RNN to process sequences of variable lengths without requiring additional parameters.
3. The input gate in an LSTM controls what new information is added to the memory cell. It decides which values from the current input and previous hidden state will be used to update the cell state, allowing the network to selectively incorporate relevant information.
4. Pooling layers in CNNs perform downsampling, reducing the spatial size of the feature maps. This decreases the number of parameters and computation required, while also making the model more invariant to small changes in the input, such as rotations or translations.
5. Vanishing gradients occur in deep neural networks when gradients become extremely small during backpropagation, preventing the weights of earlier layers from being effectively updated. This makes it difficult for the network to learn long-term dependencies or capture relevant features from the input data, hindering overall performance.
6. Advantages of character-based tokenization include no unknown words and a smaller number of types, which can be useful for languages where characters carry information. Disadvantages include that a character usually does not have a meaning, and that the models have larger sequences to process.
7. Residual blocks introduce skip connections that allow the input to bypass one or more layers. This helps to mitigate the vanishing gradient problem, enabling the training of very deep networks by facilitating the flow of gradients through the network.
8. Truncated BPTT is a technique used to address the computational cost and gradient issues associated with BPTT in very long sequences. Instead of calculating the gradient at every time step, it calculates the gradient at only a few time steps.
9. In natural language processing, a token is an instance of a sequence of characters, a type is the class of all tokens containing the same character sequence, and the vocabulary is the collection of all types. For example, in the sentence "The cat sat on the mat," there are 6 tokens, 5 types ("the" is repeated), and the vocabulary consists of those 5 unique words.
10. Depthwise separable convolutions are a technique used to reduce the computational cost of CNNs by decomposing a standard convolution into two separate operations: a depthwise convolution followed by a pointwise convolution. This approach significantly reduces the number of multiplications needed while still achieving comparable performance.

## Essay Questions

1. Compare and contrast RNNs, LSTMs, and GRUs. In what scenarios might one architecture be preferred over another? Explain your reasoning.
2. Discuss the problem of vanishing and exploding gradients in RNNs. What techniques have been developed to mitigate these issues, and how effective are they?
3. Explain the concept of backpropagation through time (BPTT) and its significance in training RNNs. Also, how does backpropagation in CNNs differ from BPTT?
4. Describe the evolution of CNN architectures from LeNet to ResNet. What were the key innovations of each architecture, and how did they contribute to improvements in image recognition performance?
5. Discuss the applications of RNNs and CNNs in natural language processing (NLP). Provide examples of how these architectures are used in tasks such as sentiment analysis, machine translation, and text generation.

## Glossary of Key Terms

- **Activation Function:** A function applied to the output of a neuron or layer, introducing non-linearity to the network and enabling it to learn complex patterns.
- **Backpropagation Through Time (BPTT):** An algorithm used to train RNNs by unfolding the network through time and applying backpropagation to calculate gradients and update weights.
- **Convolutional Neural Network (CNN):** A type of neural network that uses convolutional layers to extract features from data, commonly used for image recognition and processing.
- **Cross-Entropy Loss:** A loss function used in classification tasks to measure the difference between predicted probability distributions and actual labels.
- **Depthwise Separable Convolution:** A convolution operation that separates the spatial filtering and channel mixing stages, reducing the computational cost of CNNs.
- **Exploding Gradients:** A problem that occurs during backpropagation when gradients become very large, leading to unstable training and divergence.
- **Feature Map:** The output of a convolutional layer, representing the learned features from the input data.
- **Forget Gate:** A component of an LSTM network that determines which information from the previous cell state should be discarded.
- **Gated Recurrent Unit (GRU):** A simplified version of the LSTM that uses two gates (reset and update) to control the flow of information.
- **Input Gate:** A component of an LSTM network that controls which new information should be added to the cell state.
- **Long Short-Term Memory (LSTM):** A type of RNN architecture that incorporates memory cells and gates to address the vanishing gradient problem and capture long-term dependencies.
- **Logits:** Un-normalized outputs of a neural network layer, typically before passing through an activation function like softmax.
- **Output Gate:** A component of an LSTM network that controls which information from the cell state should be output as the hidden state.
- **Pooling:** A downsampling operation in CNNs that reduces the spatial size of feature maps, decreasing the number of parameters and computation.
- **Recurrent Neural Network (RNN):** A type of neural network designed to handle sequential data by maintaining a "memory" of past inputs.
- **Residual Block:** A building block in ResNet architectures that uses skip connections to pass the input directly to later layers, mitigating the vanishing gradient problem.
- **Skip Connection:** A connection that bypasses one or more layers in a neural network, allowing the input to be directly added to the output of a later layer.
- **Tokenization:** The process of breaking text into smaller units, i.e., tokens.
- **Truncated Backpropagation Through Time (Truncated BPTT):** A technique used to approximate BPTT in long sequences by limiting the number of time steps used for backpropagation.
- **Vanishing Gradients:** A problem that occurs during backpropagation when gradients become very small, preventing the weights of earlier layers from being effectively updated.
- **Weight Sharing:** A technique used in RNNs where the same weights are applied at each time step, reducing the number of parameters and enabling the network to process variable-length sequences.