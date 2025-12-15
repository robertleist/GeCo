from .geco import GeCo


def build_model(args):
    assert args.reduction in [4, 8, 16]

    return GeCo(
        image_size=args.image_size,
        num_objects=args.num_objects,
        zero_shot=args.zero_shot,
        emb_dim=args.emb_dim,
        num_heads=args.num_heads,
        kernel_dim=args.kernel_dim,
        train_backbone=args.backbone_lr > 0,
        reduction=args.reduction,
        model_path=args.model_path,
        inference_mode=True,
        return_masks=args.output_masks
    )
