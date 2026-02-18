# ArguGraph
Structural reasoning reconstruction demo 
ArguGraph is an AI-assisted system for reconstructing and visualizing the argumentative structure of student essays. Rather than evaluating writing through surface features such as length, vocabulary, or grammatical fluency, ArguGraph models how ideas are organized, connected, and justified.

Each essay is segmented into independent propositions and annotated with hierarchical parent–child relationships to form a reference structure. We fine-tune a transformer encoder to predict these parent–child attachments. At inference time, the model ranks candidate parents for each proposition and selects the highest-scoring attachment, reconstructing a full argument tree.

We compare two structural representations. The Collapsed model restricts attachment to observable textual segments, while the Expanded model preserves abstract coordination nodes in the hierarchy. Results show a clear interaction with structural complexity: collapsed representations perform better on simpler essays, whereas expanded representations better capture deeper coordination in complex essays.

A live demo is available at:
https://argugraphers.streamlit.app/

The app allows users to explore essays, compare reference and model-generated structures, and examine structural metrics such as depth, width, and ranking accuracy. ArguGraph demonstrates that transformer-based models can approximate argumentative structure and supports scalable structural diagnostics in writing assessment.
