import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2412   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2412.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02573._CH', 'ED6_DT07/CH02573P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH02593._CH', 'ED6_DT07/CH02593P._CP'),
        ('ED6_DT07/CH02503._CH', 'ED6_DT07/CH02503P._CP'),
        ('ED6_DT07/CH02633._CH', 'ED6_DT07/CH02633P._CP'),
        ('ED6_DT07/CH02643._CH', 'ED6_DT07/CH02643P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = -3700,
            z                   = 0,
            y                   = 14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '水壶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703941,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克拉姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '波利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛丽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '达尼艾尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x242
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_269',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 0, 0, 4200, 0)
    CreateThread(0x0010, 0x00, 0x00, func_03_2BE)

    Jump('loc_275')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_275',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_283',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_07_1A07)

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_294',
    )

    MapSetFlags(0x10000000)
    Event(0, func_06_1191)

    def _loc_294(): pass

    label('loc_294')

    Return()

# id: 0x0001 offset: 0x295
@scena.Code('func_01_295')
def func_01_295():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A7',
    )

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2A7(): pass

    label('loc_2A7')

    Return()

# id: 0x0002 offset: 0x2A8
@scena.Code('func_02_2A8')
def func_02_2A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2A8')

    def _loc_2BD(): pass

    label('loc_2BD')

    Return()

# id: 0x0003 offset: 0x2BE
@scena.Code('func_03_2BE')
def func_03_2BE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E1',
    )

    OP_8D(0x00FE, -1720, 8440, 1470, 870, 2000)

    Jump('func_03_2BE')

    def _loc_2E1(): pass

    label('loc_2E1')

    Return()

# id: 0x0004 offset: 0x2E2
@scena.Code('func_04_2E2')
def func_04_2E2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A57',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 1, 0x20B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_753',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-2590, 0, 15070, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2780, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0102, -4040, 0, 13240, 0)
    ChrSetPos(0x0101, -3050, 0, 13440, 0)
    ChrSetPos(0x00F8, -3980, 0, 12140, 0)
    ChrSetPos(0x00F9, -2940, 0, 12340, 0)
    ChrSetDirection(0x00FE, 180, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0390360369V#750F#5P艾丝蒂尔……\n',
            '还有约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360370V#751F衷心欢迎你们到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360371V#1035F#6P院长老师……\n',
            '……让您担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0390360372V#750F#5P约修亚，今后请务必\n',
            '待在艾丝蒂尔身边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360373V#751F我的希望仅此而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360374V#1054F#6P……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360375V#1017F#4P特蕾莎老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390360376V#751F#5P呵呵，看来也没有\n',
            '担心的必要呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360377V#750F科洛丝\n',
            '想必也放心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360378V#1004F#4P这么说来……',
            TxtCtl.Enter,
            '\n',
            '#1015F老师，说到科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390360379V#754F#5P嗯嗯，好像在王都呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360380V#750F基库送来了\n',
            '她的信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360381V#1016F#4P啊哈哈，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360382V#1049F#6P不愧是基库呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390360383V#754F#5P看起来科洛丝\n',
            '也有不少麻烦呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360384V从字面上看来，似乎\n',
            '已经下定决心面对\n',
            '自己的烦恼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360385V#750F虽然我并不明白\n',
            '那是怎样的决心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360386V但相信那孩子\n',
            '一定能找到自己的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360390V#1004F#4P特蕾莎老师……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360391V#1006F嗯，我也这么想！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0416, 1, 0x20B1))
    EventEnd(0x00)
    OP_4B(0x00FE, 255)

    Jump('loc_A54')

    def _loc_753(): pass

    label('loc_753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_8C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_80B',
    )

    ChrTalk(
        0x0008,
        (
            '#0390360387V#757F科洛丝的信里，\n',
            '表达出正视烦恼\n',
            '的决心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360388V#754F虽然我并不明白\n',
            '那是怎样的决心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360389V#750F但相信那孩子\n',
            '一定能找到自己的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C1')

    def _loc_80B(): pass

    label('loc_80B')

    ChrTalk(
        0x0008,
        (
            '#0390360392V#750F迫降飞艇上的士兵\n',
            '似乎暂时在做警备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360393V看起来很疲劳的样子，\n',
            '我想待会儿\n',
            '沏点草药茶给他们送去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360394V#751F不介意的话，艾丝蒂尔你们\n',
            '也随便用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C1(): pass

    label('loc_8C1')

    Jump('loc_A54')

    def _loc_8C4(): pass

    label('loc_8C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_975',
    )

    ChrTalk(
        0x0008,
        (
            '#0390360387V#757F科洛丝的信里，\n',
            '表达出正视烦恼\n',
            '的决心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360388V#754F虽然我并不明白\n',
            '那是怎样的决心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360389V#750F但相信那孩子\n',
            '一定能找到自己的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A54')

    def _loc_975(): pass

    label('loc_975')

    ChrTalk(
        0x0008,
        (
            '#0390360398V#754F由于魔兽骚乱，\n',
            '前几天都在玛诺利亚避难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360399V#757F还以为总算可以回家了\n',
            '却又马上发生了这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360400V#750F不过，真不可思议啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390360401V#751F只要孩子们露出笑脸\n',
            '就感觉总会有办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A54(): pass

    label('loc_A54')

    Jump('loc_D2B')

    def _loc_A57(): pass

    label('loc_A57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_A61',
    )

    Jump('loc_D2B')

    def _loc_A61(): pass

    label('loc_A61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_B6A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AD6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0390210108V#751F孩子们也在衷心期待\n',
            '考试结束呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210109V考试一结束，\n',
            '科洛丝\n',
            '又会来玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B67')

    def _loc_AD6(): pass

    label('loc_AD6')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0390210110V#750F学院的考试\n',
            '也快结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210111V孩子们也在衷心期待\n',
            '考试结束呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210112V#751F考试一结束，\n',
            '科洛丝\n',
            '又会来玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B67(): pass

    label('loc_B67')

    Jump('loc_D2B')

    def _loc_B6A(): pass

    label('loc_B6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_C5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BD1',
    )

    ChrTalk(
        0x0008,
        (
            '#0390210106V#751F在卢安的期间，\n',
            '方便的话请再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210107V孩子们也在等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5A')

    def _loc_BD1(): pass

    label('loc_BD1')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0390210103V#750F今天真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210104V还麻烦你们\n',
            '去接孩子们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210105V#751F方便的话请再来哦。\n',
            '孩子们也在等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5A(): pass

    label('loc_C5A')

    Jump('loc_D2B')

    def _loc_C5D(): pass

    label('loc_C5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Return,
        ),
        'loc_D2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CCF',
    )

    ChrTalk(
        0x0008,
        (
            '#0390210099V#750F玛诺利亚村在梅威海道\n',
            '往西走的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210100V那么，孩子们就\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2B')

    def _loc_CCF(): pass

    label('loc_CCF')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0390210101V#750F玛诺利亚村的\n',
            '主日学校也快结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210102V孩子们就\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2B(): pass

    label('loc_D2B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xD2F
@scena.Code('func_05_D2F')
def func_05_D2F():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_118D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 5, 0x20ED)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EAE',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)
    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0420360458V#1723F哇……\n',
            '是约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360459V#1040F达尼艾尔……好久不见了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360460V有乖乖听话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0420360461V#1721F嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360462V#1720F我也和克拉姆一样\n',
            '在帮老师干活哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360463V今天也帮菜叶\n',
            '浇水了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360464V#1049F是吗……\n',
            '达尼艾尔真了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0420360465V#1721F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x041D, 5, 0x20ED))

    Jump('loc_118D')

    def _loc_EAE(): pass

    label('loc_EAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_10B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F24',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0420360462V#1720F我也和克拉姆一样\n',
            '在帮老师干活哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360463V今天也帮菜叶\n',
            '浇水了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B5')

    def _loc_F24(): pass

    label('loc_F24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1056',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0420360468V#1720F对了，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360469V#1011F嗯？什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0420360470V#1720F姐姐\n',
            '会做苹果派吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360471V#1015F唔、嗯～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360472V#1007F对、对不起哦。\n',
            '不太会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0420360473V#1723F嗯～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360474V#1720F还是只能拜托\n',
            '科洛丝姐姐了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_10B5')

    def _loc_1056(): pass

    label('loc_1056')

    ChrTalk(
        0x00FE,
        (
            '#0420360475V#1720F如果科洛丝姐姐来了\n',
            '就要她做苹果派。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360476V#1721F姐姐做的最棒了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B5(): pass

    label('loc_10B5')

    Jump('loc_118D')

    def _loc_10B8(): pass

    label('loc_10B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1127',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0420360462V#1720F我也和克拉姆一样\n',
            '在帮老师干活哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360463V今天也给菜叶\n',
            '浇水了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118D')

    def _loc_1127(): pass

    label('loc_1127')

    ChrTalk(
        0x00FE,
        (
            '#0420360479V#1720F最近的夜晚\n',
            '真是一片漆黑啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420360480V虽然星星是很漂亮\n',
            '不过还是有点可怕呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_118D(): pass

    label('loc_118D')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0x1191
@scena.Code('func_06_1191')
def func_06_1191():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11A2',
    )

    Call(0, 0x0008)

    def _loc_11A2(): pass

    label('loc_11A2')

    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x00F7, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0008, 1)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_11D0',
    )

    ChrSetChipByIndex(0x0103, 3)

    Jump('loc_11D5')

    def _loc_11D0(): pass

    label('loc_11D0')

    ChrSetChipByIndex(0x0106, 4)

    def _loc_11D5(): pass

    label('loc_11D5')

    ChrSetPos(0x0101, -5240, 200, 7350, 90)
    ChrSetPos(0x00F7, -5240, 200, 6050, 90)
    ChrSetPos(0x0008, -2550, 200, 7350, 270)
    ChrSetPos(0x0009, -3710, 700, 6060, 0)
    ChrSetPos(0x000A, -4550, 700, 6860, 0)
    ChrSetPos(0x000B, -4530, 700, 6060, 0)
    ChrSetPos(0x000C, -3810, 700, 6860, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(-3770, 100, 7530, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010210065V#1007F#6P唉……真难为情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210066V难得想展示一下\n',
            '成为正游击士的身姿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210067V#751F呵呵，这么说来\n',
            '你成为正游击士了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210068V恭喜恭喜，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210069V#1016F#6P哪里，啊哈哈……\n',
            '其实还是新手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210070V#1026F啊，这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210071V老师刚才提到\n',
            '科洛丝有烦恼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210072V#750F嗯嗯、是艾丝蒂尔\n',
            '和约修亚的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210073V#754F重要的人感到痛苦，\n',
            '自己却无法帮上忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210074V这对那孩子来说\n',
            '大概是最难过的事了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210075V#1004F#6P重要的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210076V#1008F嘿嘿，虽然有点不好意思\n',
            '但还是觉得很高兴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210077V要早点去见见科洛丝才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210078V#750F记得现在学院是考试期间，\n',
            '可能进不去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210079V应该很快就会结束了，\n',
            '马上就能见面了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210080V#1017F#6P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210081V话虽如此……\n',
            '孩子们还真慢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210082V主日学校的授课\n',
            '不会那么长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210083V#750F难道是下课以后\n',
            '还留在村里玩了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210084V听说新来的巡回神父\n',
            '很喜欢小孩子的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210085V#1015F#6P新来的巡回神父……\n',
            '（咦……好像在哪里听过？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00F7, 1)
    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_172A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210086V#051F#4P那就去玛诺利亚村\n',
            '确认一下情况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210087V顺便把孩子们\n',
            '送回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1798')

    def _loc_172A(): pass

    label('loc_172A')

    ChrTalk(
        0x0103,
        (
            '#0030210088V#020F#4P那么，去玛诺利亚村\n',
            '确认一下可能比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210089V顺便把孩子们\n',
            '送回这里就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1798(): pass

    label('loc_1798')

    ChrSetSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010210090V#1006F#3P啊，那倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210091V#753F哎呀……可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010210092V#1001F#6P嘿嘿。\n',
            '请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210093V算是美味茶点的回礼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1887',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210094V#051F#4P还要回\n',
            '受人安慰的礼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BA')

    def _loc_1887(): pass

    label('loc_1887')

    ChrTalk(
        0x0103,
        (
            '#0030210095V#021F#4P还要回\n',
            '被紧紧抱住的礼呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18BA(): pass

    label('loc_18BA')

    ChrSetSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010210096V#1013F#3P讨、讨厌……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210097V#751F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210098V#750F明白了。\n',
            '那么就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0101, -3650, 0, 8410, 90)
    ChrSetPos(0x00F7, -3650, 0, 8410, 90)
    ChrSetPos(0x0008, -3700, 0, 14600, 0)
    CameraMove(-3650, 0, 8410, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    OP_28(0x0082, 0x02, 0x0080)
    OP_28(0x0082, 0x01, 0x0100)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1A07
@scena.Code('func_07_1A07')
def func_07_1A07():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A18',
    )

    Call(0, 0x0008)

    def _loc_1A18(): pass

    label('loc_1A18')

    EventBegin(0x00)
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x00F7, 0x0004)
    ChrSetFlags(0x0109, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x000D, 11)
    ChrSetChipByIndex(0x000E, 12)
    ChrSetChipByIndex(0x000F, 13)
    ChrSetChipByIndex(0x0010, 14)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetFlags(0x0010, 0x0004)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x00F7, -5240, 200, 4750, 90)
    ChrSetPos(0x0010, -2550, 200, 4750, 0)
    ChrSetPos(0x0109, -3850, 200, 3900, 12)
    ChrSetPos(0x0008, -3930, 200, 8250, 180)
    ChrSetPos(0x000F, -5240, 200, 7350, 90)
    ChrSetPos(0x0101, -5240, 200, 6050, 90)
    ChrSetPos(0x000D, -2550, 200, 7350, 270)
    ChrSetPos(0x000E, -2550, 200, 6050, 270)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x109, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x109, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x109, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0109, 10)
    ChrSetChipByIndex(0x0008, 1)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1B57',
    )

    ChrSetChipByIndex(0x0103, 3)

    Jump('loc_1B5C')

    def _loc_1B57(): pass

    label('loc_1B57')

    ChrSetChipByIndex(0x0106, 4)

    def _loc_1B5C(): pass

    label('loc_1B5C')

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0390210241V#750F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210242V神父和艾丝蒂尔\n',
            '认识啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210243V#751F呵呵，世界真是小啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210244V#1061F呀～真是这么回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210245V#1062F话说回来，\n',
            '还准备了我的午饭，\n',
            '真是对老师不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210246V#750F哪里哪里，反正是顺便做的，\n',
            '你教孩子们学习\n',
            '这是应该的谢礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ChrTalk(
        0x000D,
        (
            '#0400210247V#775F对了，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210248V约修亚哥哥不在，\n',
            '今天没一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010210249V#1025F#6P啊，嗯……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210250V他有点事，\n',
            '没一起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210251V#1067F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0420210252V#1723F这样啊……好失望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0400210253V#773F呜～还想让约修亚哥哥\n',
            '也看看孤儿院\n',
            '恢复原状的样子呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0410210254V#1716F真是可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0430210255V#1730F#2P他当公主的样子\n',
            '也想再看看呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210256V#1016F#6P啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210257V#1011F话说回来，\n',
            '主日学校课时真长啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210258V最后好像在读什么，\n',
            '是小说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0400210259V#770F哼哼。\n',
            '叫做『人偶骑士』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210260V是以人偶师的战斗为主题，\n',
            '紧张刺激的动作剧哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ChrTalk(
        0x000F,
        (
            '#0410210261V#1712F啊，不对啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210262V#1718F不是以身份不同的恋爱为主题的\n',
            '浪漫爱情故事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210263V#1068F来利贝尔时带来的\n',
            '青少年向小说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210264V本来只是打算\n',
            '一点点读给他们听的，\n',
            '一不小心就读了全卷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010210265V#1016F#6P啊哈哈。\n',
            '你就别抱怨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210266V#751F呵呵。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210267V#750F神父大人今后\n',
            '打算回卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210268V#1062F嗯嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210269V还有其它的村子要巡回，\n',
            '应该很快就要\n',
            '上定期船了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210270V#1060F这么说来，艾丝蒂尔\n',
            '怎么会在卢安地区？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210271V还是游击士的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210272V#1006F#6P嗯，发生了不少事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210273V#1004F对了，我们\n',
            '来孤儿院是想\n',
            '打听一件事的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    ChrSetSubChip(0x0008, 2)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0390210274V#750F是波利见到的\n',
            '『白衣叔叔』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x000D,
        (
            '#0400210275V#770F啊～那件事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0430210276V#1733F#2P嗯～？\n',
            '波利怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)

    ChrTalk(
        0x0101,
        (
            '#0010210277V#1011F#6P嗯，有点事\n',
            '想要打听一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210278V『白衣叔叔』的事\n',
            '能不能详细告诉我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0430210279V#1731F#2P白衣叔叔\n',
            '就是白衣叔叔嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210280V#1732F#2P骨碌骨碌地转着圈，\n',
            '看起来很快乐的样子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210281V#1016F#6P嗯……不是很明白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ChrTalk(
        0x000F,
        (
            '#0410210282V#1710F嗯，让我\n',
            '来说明吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210283V#1900F那是４天前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210284V这孩子晚饭之后\n',
            '跑去外边发呆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210285V#1710F然后天上好像\n',
            '浮现出一个白色的男子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0430210286V#1730F#2P是啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210287V#2P很高兴的飞来跳去，\n',
            '在天空骨碌骨碌地跳着舞～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210288V#2P波利一跟他说话\n',
            '他就鞠躬行了个礼，\n',
            '然后就飞走了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ChrTalk(
        0x000D,
        (
            '#0400210289V#772F我看啊～\n',
            '只是你睡迷糊了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210290V如果说是幽灵的话\n',
            '完全不可怕嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210291V#754F我一开始也是这么想，\n',
            '但是达尼艾尔好像也看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210292V#750F对吧，达尼艾尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    ChrTalk(
        0x0010,
        (
            '#0420210293V#1720F嗯。\n',
            '我只看到一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420210294V白色的奇怪影子，往东边\n',
            '咻的一下就飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210295V#1007F#6P嗯、嗯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2759',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210296V#552F有两个目击者，\n',
            '可信性似乎就很高了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210297V#053F不过，一搭话\n',
            '就行礼吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210298V#051F那个白衣叔叔，\n',
            '看到他长什么样子了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2803')

    def _loc_2759(): pass

    label('loc_2759')

    ChrTalk(
        0x0103,
        (
            '#0030210299V#522F目击者有两个，\n',
            '可信度就变高了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210300V#026F话说回来，一搭话\n',
            '就行了个礼啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210301V#020F对了，那个白衣叔叔，\n',
            '看到他长什么样子了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2803(): pass

    label('loc_2803')

    ChrTalk(
        0x000E,
        (
            '#0430210302V#1733F#2P脸没看到～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210303V#1730F#2P因为叔叔\n',
            '戴着奇怪的面具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210304V#1004F#6P面、面具！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_28EE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210305V#055F这实在是……\n',
            '奇怪的幽灵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2924')

    def _loc_28EE(): pass

    label('loc_28EE')

    ChrTalk(
        0x0103,
        (
            '#0030210306V#023F怎么说呢……\n',
            '相当诡异的幽灵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2924(): pass

    label('loc_2924')

    ChrTalk(
        0x000D,
        (
            '#0400210307V#775F我说啊，波利。\n',
            '这种事你早说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210308V我可是第一次听到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0430210309V#1733F#2P但是谁也\n',
            '没问过我嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 2)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0390210310V#750F嗯，面具暂且不管，\n',
            '看来好像不是梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210311V慎重起见，我还是通知了\n',
            '游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210312V从那以后，虽然多加注意，\n',
            '但好像没有再次出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010210313V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00F7, 1)
    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2AD5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210314V#051F大致上明白了。\n',
            '得了不少参考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B11')

    def _loc_2AD5(): pass

    label('loc_2AD5')

    ChrTalk(
        0x0103,
        (
            '#0030210315V#021F情况明白了。\n',
            '应该算是掌握了不少信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B11(): pass

    label('loc_2B11')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2B2E
@scena.Code('func_08_2B2E')
def func_08_2B2E():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2BA8'),
        (0x00000001, 'loc_2BAE'),
        (-1, 'loc_2BB4'),
    )

    def _loc_2BA8(): pass

    label('loc_2BA8')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2BB4')

    def _loc_2BAE(): pass

    label('loc_2BAE')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2BB4')

    def _loc_2BB4(): pass

    label('loc_2BB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2BC2',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_2BC6')

    def _loc_2BC2(): pass

    label('loc_2BC2')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_2BC6(): pass

    label('loc_2BC6')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
