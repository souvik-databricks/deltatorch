from typing import Optional, Callable, List, Any

from torch.utils.data import DataLoader

from .deltadataset import FieldSpec
from .id_based_deltadataset import IDBasedDeltaDataset


def create_pytorch_dataloader(
    path: str,
    id_field: str,
    fields: List[FieldSpec],
    batch_size: int = None,
    collate_fn: Optional[Callable[[List], Any]] = None,
    use_fixed_rank: bool = False,
    rank: int = None,
    num_ranks: int = None,
    num_workers: int = 2,
    shuffle: bool = False,
    timeout: int = 15,
    queue_size: int = 25000,
):
    dataset = IDBasedDeltaDataset(
        path,
        id_field,
        fields,
        use_fixed_rank,
        rank,
        num_ranks,
        num_workers,
        shuffle,
        timeout,
        queue_size,
    )

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0,
        collate_fn=collate_fn,
    )
