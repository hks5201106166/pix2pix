from .base_options import BaseOptions


class TestOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        # Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')
        # rewrite devalue values
        parser.set_defaults(model='test')
        # To avoid cropping, the load_size should be the same as crop_size
        parser.set_defaults(load_size=parser.get_default('crop_size'))
        self.isTrain = False
       #
       #  parser.add_argument('--display_freq', type=int, default=400,
       #                      help='frequency of showing training results on screen')
       #  parser.add_argument('--display_ncols', type=int, default=4,
       #                      help='if positive, display all images in a single visdom web panel with certain number of images per row.')
       #  parser.add_argument('--display_id', type=int, default=1, help='window id of the web display')
       #  parser.add_argument('--display_server', type=str, default="http://localhost",
       #                      help='visdom server of the web display')
       #  parser.add_argument('--display_env', type=str, default='main',
       #                      help='visdom display environment name (default is "main")')
       #  parser.add_argument('--display_port', type=int, default=8097, help='visdom port of the web display')
       #  parser.add_argument('--update_html_freq', type=int, default=1000,
       #                      help='frequency of saving training results to html')
       #  parser.add_argument('--print_freq', type=int, default=100,
       #                      help='frequency of showing training results on console')
       #  parser.add_argument('--no_html', action='store_true',
       #                      help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
       #  # network saving and loading parameters
       #  parser.add_argument('--save_latest_freq', type=int, default=1000, help='frequency of saving the latest results')
       #  parser.add_argument('--save_epoch_freq', type=int, default=1,
       #                      help='frequency of saving checkpoints at the end of epochs')
       #  parser.add_argument('--save_by_iter', action='store_true', help='whether saves model by iteration')
       #  parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
       #  parser.add_argument('--epoch_count', type=int, default=1,
       #                      help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
       # # parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
       #  # training parameters
       #  parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
       #  parser.add_argument('--niter_decay', type=int, default=100,
       #                      help='# of iter to linearly decay learning rate to zero')
       #  parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
       #  parser.add_argument('--lr', type=float, default=0.002, help='initial learning rate for adam')
       #  parser.add_argument('--gan_mode', type=str, default='lsgan',
       #                      help='the type of GAN objective. [vanilla| lsgan | wgangp]. vanilla GAN loss is the cross-entropy objective used in the original GAN paper.')
       #  parser.add_argument('--pool_size', type=int, default=50,
       #                      help='the size of image buffer that stores previously generated images')
       #  parser.add_argument('--lr_policy', type=str, default='linear',
       #                      help='learning rate policy. [linear | step | plateau | cosine]')
       #  parser.add_argument('--lr_decay_iters', type=int, default=50,
       #                      help='multiply by a gamma every lr_decay_iters iterations')
       #
       #  self.isTrain = True
        return parser



