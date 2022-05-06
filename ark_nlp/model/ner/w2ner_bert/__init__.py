from ark_nlp.model.ner.w2ner_bert.w2ner_named_entity_recognition_dataset import W2nerDataset as Dataset
from ark_nlp.dataset import BIONERDataset as CrfBertNERDataset

from ark_nlp.processor.tokenizer.transfomer import TokenTokenizer as Tokenizer
from ark_nlp.processor.tokenizer.transfomer import TokenTokenizer as W2NERTokenizer

from ark_nlp.nn import BertConfig as W2nerBertConfig
from ark_nlp.nn import BertConfig as ModuleConfig

from ark_nlp.model.ner.w2ner_bert.w2ner_bert import W2NERBert
from ark_nlp.model.ner.w2ner_bert.w2ner_bert import W2NERBert as Module

from ark_nlp.factory.optimizer import get_default_crf_bert_optimizer as get_default_model_optimizer
from ark_nlp.factory.optimizer import get_default_crf_bert_optimizer as get_default_crf_bert_optimizer

from ark_nlp.model.ner.w2ner_bert.w2ner_named_entity_recognition_task import W2NERTask as Task
from ark_nlp.factory.task import BIONERTask as CrfBertNERTask

from ark_nlp.model.ner.w2ner_bert.w2ner_named_entity_recognition_predictor import W2NERPredictor as Predictor
from ark_nlp.model.ner.w2ner_bert.w2ner_named_entity_recognition_predictor import W2NERPredictor as CrfBertNERPredictor