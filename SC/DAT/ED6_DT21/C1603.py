import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1603_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1603   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1603.x'
    header.mapIndex       = 1
    header.bgm            = 125
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
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT26/CH20340._CH', 'ED6_DT26/CH20340P._CP'),
        ('ED6_DT06/CH20091._CH', 'ED6_DT06/CH20091P._CP'),
        ('ED6_DT26/CH20341._CH', 'ED6_DT26/CH20341P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00132._CH', 'ED6_DT07/CH00132P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00142._CH', 'ED6_DT07/CH00142P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00155._CH', 'ED6_DT07/CH00155P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT06/CH20085._CH', 'ED6_DT06/CH20085P._CP'),
        ('ED6_DT26/CH20282._CH', 'ED6_DT26/CH20282P._CP'),
        ('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP'),
        ('ED6_DT26/CH20352._CH', 'ED6_DT26/CH20352P._CP'),
        ('ED6_DT26/CH20353._CH', 'ED6_DT26/CH20353P._CP'),
    ]

# id: 0x10001 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '银发的青年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '怀斯曼教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古代龙',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '龙',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048609,
            chipIndex           = 33,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048609,
            chipIndex           = 33,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金耀石块·艾丝蒂尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048609,
            chipIndex           = 33,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金耀石块·阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048609,
            chipIndex           = 33,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x2BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2BA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2BA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0001, 0x0004)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_344)

    Jump('loc_302')

    def _loc_2DE(): pass

    label('loc_2DE')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2EA'),
        (-1, 'loc_302'),
    )

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0345, 1, 0x1A29)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_71(0x0001, 0x0004)
    Event(0, func_04_D5C)

    def _loc_2FF(): pass

    label('loc_2FF')

    Jump('loc_302')

    def _loc_302(): pass

    label('loc_302')

    Return()

# id: 0x0001 offset: 0x303
@scena.Code('func_01_303')
def func_01_303():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x44F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_325',
    )

    ExecExpressionWithVar(
        0x29,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x36),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_2266)

    def _loc_325(): pass

    label('loc_325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Return,
        ),
        'loc_33E',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_72(0x0003, 0x0002)

    Jump('loc_343')

    def _loc_33E(): pass

    label('loc_33E')

    OP_71(0x0003, 0x0002)

    def _loc_343(): pass

    label('loc_343')

    Return()

# id: 0x0002 offset: 0x344
@scena.Code('func_02_344')
def func_02_344():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-270, 0, -16520, 0)
    OP_67(0, 5490, -10000, 0)
    CameraSetDistance(2690, 0)
    OP_6C(200000, 0)
    OP_6E(360, 0)
    ChrSetPos(0x0009, 3570, 0, -26960, 0)
    ChrSetPos(0x0008, 2570, 0, -27960, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 970)
    MapSetFlags(0x00000010)
    OP_11(0xC8, 0xC8, 0xC8, 25000, 38000, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_03F8')
    def lambda_03F8():
        ChrWalkTo(0x00FE, 590, 0, -15340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_03F8)

    Sleep(300)

    ChrWalkTo(0x0008, -500, 0, -16300, 2000, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140300043V#126F#5P……这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0150300044V#1154F#5P哈哈哈……\n',
            '果然在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300045V#1150F看，莱维。\n',
            '这是多么优美的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140300046V#124F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140300047V#120F#2P真的要用这种东西\n',
            '进行实验吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0150300048V#1150F#6P你会有所顾虑也是理所当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300049V但是，要完成『β』\n',
            '无论如何都必须得到这些数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300050V…………你们是……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x0008, 0x00, 0x00, func_03_D14)

    @scena.Lambda('lambda_065D')
    def lambda_065D():
        CameraMove(1720, 4250, -8690, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_065D)

    @scena.Lambda('lambda_0675')
    def lambda_0675():
        OP_67(0, 1070, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0675)

    @scena.Lambda('lambda_068D')
    def lambda_068D():
        CameraSetDistance(3230, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_068D)

    @scena.Lambda('lambda_069D')
    def lambda_069D():
        OP_6C(351000, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_069D)

    @scena.Lambda('lambda_06AD')
    def lambda_06AD():
        OP_6E(553, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_06AD)

    OP_B0(0x0000, 0x05)
    OP_6F(0x0000, 980)
    OP_70(0x0000, 920)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 920)
    OP_70(0x0000, 870)

    ChrTalk(
        0x0009,
        (
            '#0150300051V#1153F#5P哦哦……\n',
            '好像醒了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300052V#1154F时隔２０年的觉醒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300053V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0150300054V#1150F#5P初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300055V本人名叫盖鲁格·怀斯曼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300056V是负责掌管『噬身之蛇』的\n',
            '『蛇之使徒』的成员之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300057V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490300058V……滚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490300059V虽然你身体里蕴藏着的力量……\n',
            '依然还有一丝让人怀念的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490300060V不过，我不喜欢你的那种眼神……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490300061V只有邪恶，才能使你的眼中透露喜悦\n',
            '……我可以感觉到你那歪曲的灵魂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0150300062V#1151F#5P呵呵，承蒙夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300063V但是很遗憾\n',
            '你没有拒绝的权利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300064V因为是有关女神至宝的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300065V………什么………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0150300066V#1154F#5P莱维，给它看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140300067V#121F#5P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-1360, 0, -17130, 0)
    OP_67(0, 5290, -10000, 0)
    CameraSetDistance(2570, 0)
    OP_6C(206000, 0)
    OP_6E(360, 0)
    ChrSetDirection(0x0008, 0, 0)
    ChrSetDirection(0x0009, 0, 0)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    OP_99(0x0008, 0x00, 0x04, 1000)
    PlaySE(216, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(380, 100, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300068V………那是………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0150300069V#1151F#5P是否唤醒了１２００年前的记忆了呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150300070V虽然只是复制品，\n',
            '但做得很不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(380, 100, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490300071V…………你们…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490300072V……莫非要将『辉之环』！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0150300073V#1154F#5P呵呵，就是这个意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_0C25')
    def lambda_0C25():
        OP_99(0x0009, 0x00, 0x03, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0C25)

    PlayEffect(0x00, 0x00, 0x00FF, 590, 0, -15340, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    @scena.Lambda('lambda_0C6F')
    def lambda_0C6F():
        OP_99(0x0009, 0x03, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0C6F)

    PlaySE(213, 0x00, 0x64)
    Sleep(1000)

    StopEffect(0x00, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_0C91')
    def lambda_0C91():
        OP_99(0x0009, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0C91)

    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0150300074V#1155F#5P那么──\n',
            '开始最后的实验吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS145._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0100._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xD14
@scena.Code('func_03_D14')
def func_03_D14():
    Sleep(500)

    @scena.Lambda('lambda_0D1F')
    def lambda_0D1F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D1F)

    Sleep(100)

    @scena.Lambda('lambda_0D32')
    def lambda_0D32():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D32)

    Sleep(5000)

    @scena.Lambda('lambda_0D45')
    def lambda_0D45():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D45)

    @scena.Lambda('lambda_0D53')
    def lambda_0D53():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D53)

    Return()

# id: 0x0004 offset: 0xD5C
@scena.Code('func_04_D5C')
def func_04_D5C():
    Call(0, 0x0005)
    Call(0, 0x0008)

    Return()

# id: 0x0005 offset: 0xD65
@scena.Code('func_05_D65')
def func_05_D65():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D7C',
    )

    Call(0, 0x001A)
    Call(0, 0x001B)

    def _loc_D7C(): pass

    label('loc_D7C')

    CameraMove(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    CameraSetDistance(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 45000, 70000, 0)
    ChrSetPos(0x0101, 2800, 0, -25400, 0)
    ChrSetPos(0x0106, 4180, 0, -25530, 0)
    ChrSetPos(0x0107, 4310, 0, -26920, 0)
    ChrSetPos(0x00F9, 2780, 0, -26920, 0)
    OP_A1(0x000A, 0x0000)
    ChrSetPos(0x000A, 10000, 300, 14130, 192)
    OP_6F(0x0000, 970)
    OP_70(0x0000, 1040)
    ChrSetDirection(0x000B, 180, 0)
    OP_CF(0x000B, 0x00, 'Frame127_FireEmitter')
    ChrSetFlags(0x000A, 0x0001)
    ChrClearFlags(0x000A, 0x0080)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x07,
        (
            (Expr.PushLong, 0x1964),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x000007D0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F18',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F56')

    def _loc_F18(): pass

    label('loc_F18')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F3F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F56')

    def _loc_F3F(): pass

    label('loc_F3F')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_F56(): pass

    label('loc_F56')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010311002V#1020F#6P（啊啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311003V#057F#6P（在吗……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(81)
    Sleep(400)

    @scena.Lambda('lambda_0FBC')
    def lambda_0FBC():
        CameraMove(8480, 0, 16800, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FBC)

    @scena.Lambda('lambda_0FD4')
    def lambda_0FD4():
        OP_67(0, 4000, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FD4)

    @scena.Lambda('lambda_0FEC')
    def lambda_0FEC():
        CameraSetDistance(4090, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FEC)

    @scena.Lambda('lambda_0FFC')
    def lambda_0FFC():
        OP_6C(347000, 6000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0FFC)

    OP_6E(421, 6000)
    Sleep(1500)

    Fade(500)
    CameraMove(3160, 0, -25690, 0)
    OP_67(0, 9710, -10000, 0)
    CameraSetDistance(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070311004V#065F#6P（在、在睡觉吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10FA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311005V#022F#6P（嗯嗯……好像是的。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030311006V（那个叫莱维的人\n',
            '  好像也不在……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1243')

    def _loc_10FA(): pass

    label('loc_10FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1168',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311007V#043F#6P（……似乎没错。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060311008V（那个叫莱维的人\n',
            '  好像也不在……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1243')

    def _loc_1168(): pass

    label('loc_1168')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11D7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311009V#035F#6P（呼……似乎没错。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311010V#030F（好像也没看到\n',
            '莱维的身影。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1243')

    def _loc_11D7(): pass

    label('loc_11D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1243',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311011V#070F（啊啊……似乎没错。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080311012V（那个叫莱维的男人\n',
            '  好像也不在。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1243(): pass

    label('loc_1243')

    ChrTalk(
        0x0101,
        (
            '#0010311013V#1006F#6P（这可能是个机会……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    @scena.Lambda('lambda_1281')
    def lambda_1281():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1281)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010311014V#1002F#5P（阿加特、怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311015V#053F#4P（首先我一个人接近。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311016V#051F（要是顺利的话，\n',
            '  就这样把『福音』\n',
            '  一口气破坏了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311017V#1002F#5P（是吗……明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311018V#063F#6P（阿加特……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)

    ChrTalk(
        0x0106,
        (
            '#0050311019V#051F#2P（没问题，别担心。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311020V(失败的时候拜托你们掩护了。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311021V#560F#6P（是……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311022V#1006F#5P（小心哦……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1451')
    def lambda_1451():
        OP_69(0x00FE, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1451)

    @scena.Lambda('lambda_145F')
    def lambda_145F():
        OP_67(0, 5580, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_145F)

    @scena.Lambda('lambda_1477')
    def lambda_1477():
        OP_6C(336000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1477)

    @scena.Lambda('lambda_1487')
    def lambda_1487():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_1487')

    DispatchAsync2(0x0101, 0x0002, lambda_1487)

    @scena.Lambda('lambda_1498')
    def lambda_1498():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_1498')

    DispatchAsync2(0x0107, 0x0002, lambda_1498)

    @scena.Lambda('lambda_14A9')
    def lambda_14A9():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_14A9')

    DispatchAsync2(0x00F9, 0x0002, lambda_14A9)

    Sleep(500)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 23)
    ChrSetSubChip(0x0106, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrSetFlags(0x0106, 0x0004)
    OP_C4(0x00, 0x00000040)
    OP_6A(0x0106)
    Sleep(300)

    ChrSetDirection(0x0106, 0, 400)
    Sleep(300)

    ChrWalkTo(0x0106, 3930, 0, -10800, 8000, 0x00)
    ChrSetDirection(0x0106, 180, 400)
    Sleep(1000)

    OP_6A(0x00FF)
    OP_C4(0x01, 0x00000040)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0107, 0x02)
    TerminateThread(0x00F9, 0x02)

    @scena.Lambda('lambda_152C')
    def lambda_152C():
        CameraMove(6440, 0, 6810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_152C)

    @scena.Lambda('lambda_1544')
    def lambda_1544():
        CameraSetDistance(2960, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1544)

    OP_6E(206, 3000)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050311023V#057F#2P（是那个吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Sleep(200)

    Fade(500)
    CameraMove(3410, 0, -10000, 0)
    OP_67(0, 4900, -10000, 0)
    CameraSetDistance(2990, 0)
    OP_6C(336000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0106, 0x0040)
    OP_0D()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 32)
    OP_0D()
    Sleep(300)

    PlaySE(157, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp009_00.eff')

    @scena.Lambda('lambda_1616')
    def lambda_1616():
        OP_99(0x00FE, 0x01, 0x07, 1500)
        Yield()

        Jump('lambda_1616')

    DispatchAsync2(0x0106, 0x0002, lambda_1616)

    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050311024V#053F（……要上啦！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    TerminateThread(0x0106, 0x02)

    @scena.Lambda('lambda_165E')
    def lambda_165E():
        CameraMove(5910, 0, -11000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_165E)

    ChrClearFlags(0x0106, 0x0002)
    ChrSetFlags(0x0106, 0x0800)
    ChrSetChipByIndex(0x0106, 24)
    ChrSetSubChip(0x0106, 0)

    @scena.Lambda('lambda_168A')
    def lambda_168A():
        ChrSetDirection(0x00FE, 0, 600)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_168A)

    @scena.Lambda('lambda_1698')
    def lambda_1698():
        ChrJumpTo(0x00FE, 5910, 0, -11000, 200, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1698)

    WaitForThreadExit(0x0106, 0x0002)
    WaitForThreadExit(0x0106, 0x0003)

    @scena.Lambda('lambda_16C0')
    def lambda_16C0():
        CameraMove(7100, 0, 4690, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_16C0)

    ChrSetFlags(0x0106, 0x1000)

    ChrTalk(
        0x0106,
        (
            '#0050311025V#054F#6P#3S啊啊啊啊！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrWalkTo(0x0106, 7510, 0, 300, 12000, 0x00)
    TerminateThread(0x0106, 0x01)
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_172C')
    def lambda_172C():
        CameraMove(7100, 2000, 4690, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_172C)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_1749')
    def lambda_1749():
        ChrJumpTo(0x0106, 7400, 1400, 3400, 2000, 5000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_1749)

    Sleep(100)

    ChrSetChipByIndex(0x0106, 25)

    @scena.Lambda('lambda_1771')
    def lambda_1771():
        OP_99(0x00FE, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1771)

    @scena.Lambda('lambda_1781')
    def lambda_1781():
        CameraMove(6810, 0, 5420, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1781)

    @scena.Lambda('lambda_1799')
    def lambda_1799():
        OP_67(0, 7660, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1799)

    @scena.Lambda('lambda_17B1')
    def lambda_17B1():
        CameraSetDistance(2860, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17B1)

    @scena.Lambda('lambda_17C1')
    def lambda_17C1():
        OP_6C(336000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_17C1)

    Sleep(300)

    @scena.Lambda('lambda_17D6')
    def lambda_17D6():
        OP_99(0x00FE, 0x04, 0x05, 2500)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_17D6)

    OP_7C(0, 500, 3000, 800)
    WaitForThreadExit(0x0106, 0x0000)
    WaitForThreadExit(0x0106, 0x0002)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1045)
    OP_20(0x00000000)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 7850, 2000, 4370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrSetChipByIndex(0x0106, 24)
    ChrSetSubChip(0x0106, 0)

    @scena.Lambda('lambda_185B')
    def lambda_185B():
        ChrJumpTo(0x0106, 7140, 0, 1650, 100, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_185B)

    WaitForThreadExit(0x0106, 0x0000)
    ChrSetDirection(0x0106, 45, 0)
    ChrSetChipByIndex(0x0106, 25)

    @scena.Lambda('lambda_188A')
    def lambda_188A():
        OP_99(0x0106, 0x05, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_188A)

    @scena.Lambda('lambda_189A')
    def lambda_189A():
        ChrJumpTo(0x0106, 5280, 0, -1900, 500, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_189A)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    MapSetFlags(0x00000010)
    CameraMove(6460, 0, 13890, 0)
    OP_67(0, 3020, -10000, 0)
    CameraSetDistance(3800, 0)
    OP_6C(351000, 0)
    OP_6E(498, 0)
    WaitForThreadExit(0x0106, 0x0000)
    ChrSetChipByIndex(0x0106, 23)
    ChrClearFlags(0x0106, 0x0800)
    OP_0D()
    Sleep(500)

    PlaySE(300, 0x00, 0x5A)
    Sleep(2000)

    ChrTalk(
        0x0106,
        (
            '#0050311026V#054F成功了吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    LoadEffect(0x02, 'map\\\\mp007_00.eff')
    PlaySE(144, 0x00, 0x64)
    PlayEffect(0x02, 0x01, 0x000B, 900, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    @scena.Lambda('lambda_19A6')
    def lambda_19A6():
        CameraSetDistance(3380, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19A6)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 28)
    ChrSetSubChip(0x0106, 0)
    Sleep(500)

    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x19)
    OP_6F(0x0000, 970)
    OP_70(0x0000, 1040)
    ChrMoveTo(0x000A, 9900, 300, 14030, 10000, 0x00)
    ChrMoveTo(0x000A, 10000, 300, 14130, 10000, 0x00)
    ChrMoveTo(0x000A, 9900, 300, 14030, 10000, 0x00)
    ChrMoveTo(0x000A, 10000, 300, 14130, 10000, 0x00)
    ChrMoveTo(0x000A, 9900, 300, 14030, 10000, 0x00)
    ChrMoveTo(0x000A, 10000, 300, 14130, 10000, 0x00)
    OP_73(0x0000)
    StopEffect(0x01, 0x02)
    PlayBGM(54)
    Sleep(500)

    @scena.Lambda('lambda_1A82')
    def lambda_1A82():
        CameraMove(7030, 2640, 15970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A82)

    @scena.Lambda('lambda_1A9A')
    def lambda_1A9A():
        OP_67(0, 1000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A9A)

    @scena.Lambda('lambda_1AB2')
    def lambda_1AB2():
        OP_6C(15000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AB2)

    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 1045)
    OP_70(0x0000, 1070)
    PlaySE(290, 0x00, 0x64)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 125)
    OP_70(0x0000, 180)
    ChrSetDirection(0x0106, 0, 0)
    Sleep(75)

    ChrSetDirection(0x0106, 315, 0)
    Sleep(425)

    OP_23(0x0193)
    Sleep(700)

    Sleep(100)

    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    Fade(500)
    CameraMove(-840, 0, 5360, 0)
    OP_67(0, 4730, -10000, 0)
    CameraSetDistance(4190, 0)
    OP_6C(315000, 0)
    OP_6E(352, 0)
    ChrSetPos(0x0106, 3860, 0, -4770, 0)
    ChrSetDirection(0x0106, 0, 0)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 28)
    ChrSetSubChip(0x0106, 3)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050311027V#057F#5P可恶……力量太小了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BEA')
    def lambda_1BEA():
        CameraMove(-500, 1060, 12470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1BEA)

    @scena.Lambda('lambda_1C02')
    def lambda_1C02():
        OP_67(0, 3440, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C02)

    @scena.Lambda('lambda_1C1A')
    def lambda_1C1A():
        CameraSetDistance(3500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C1A)

    @scena.Lambda('lambda_1C2A')
    def lambda_1C2A():
        OP_6C(339000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C2A)

    Sleep(500)

    Sleep(200)

    LoadEffect(0x03, 'monster\\ms30703.eff')
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 120)
    Sleep(1000)

    @scena.Lambda('lambda_1C72')
    def lambda_1C72():
        CameraMove(3510, 380, 5270, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C72)

    @scena.Lambda('lambda_1C8A')
    def lambda_1C8A():
        OP_67(0, 2900, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C8A)

    @scena.Lambda('lambda_1CA2')
    def lambda_1CA2():
        CameraSetDistance(3190, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CA2)

    @scena.Lambda('lambda_1CB2')
    def lambda_1CB2():
        OP_6C(339000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CB2)

    @scena.Lambda('lambda_1CC2')
    def lambda_1CC2():
        OP_6E(462, 300)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_1CC2)

    PlayEffect(0x03, 0x00, 0x000B, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x0106, 0, 0, 0, 0)
    PlaySE(289, 0x00, 0x64)
    Sleep(100)

    CreateThread(0x0106, 0x00, 0x00, func_07_2229)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    Sleep(1000)

    ChrSetPos(0x0107, 9710, 0, -14620, 0)

    ChrTalk(
        0x0107,
        (
            '#0070311028V#2P阿加特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    LoadEffect(0x03, 'map\\\\mp019_00.eff')
    ChrSetPos(0x000C, 6500, 5510, 9600, 0)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, 14500, 5730, -23660, 0, 0, 0, 1000, 1000, 1000, 0x000B, 0, 1500, 0, 0)
    Fade(500)
    CameraMove(5000, 2150, 160, 0)
    OP_67(0, 1730, -10000, 0)
    CameraSetDistance(2610, 0)
    OP_6C(339000, 0)
    OP_6E(530, 0)
    ChrSetPos(0x0106, 8020, 0, -5130, 0)
    ChrSetSubChip(0x0106, 2)
    Sleep(1500)

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 75)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0107, 0x0040)
    ChrSetFlags(0x00F9, 0x0040)
    ChrSetPos(0x0101, 12470, 0, -15800, 0)
    ChrSetPos(0x0107, 14010, 0, -16620, 0)
    ChrSetPos(0x00F9, 13000, 0, -17160, 0)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 21)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1EB9'),
        (0x00000003, 'loc_1EC1'),
        (0x00000004, 'loc_1EC9'),
        (0x00000007, 'loc_1ED1'),
        (-1, 'loc_1ED9'),
    )

    def _loc_1EB9(): pass

    label('loc_1EB9')

    ChrSetChipByIndex(0x00F9, 9)

    Jump('loc_1ED9')

    def _loc_1EC1(): pass

    label('loc_1EC1')

    ChrSetChipByIndex(0x00F9, 12)

    Jump('loc_1ED9')

    def _loc_1EC9(): pass

    label('loc_1EC9')

    ChrSetChipByIndex(0x00F9, 15)

    Jump('loc_1ED9')

    def _loc_1ED1(): pass

    label('loc_1ED1')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_1ED9')

    def _loc_1ED9(): pass

    label('loc_1ED9')

    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0107, 0x1000)
    ChrSetFlags(0x00F9, 0x1000)

    @scena.Lambda('lambda_1EEE')
    def lambda_1EEE():
        ChrWalkTo(0x00FE, 7030, 0, -5610, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1EEE)

    @scena.Lambda('lambda_1F09')
    def lambda_1F09():
        ChrWalkTo(0x00FE, 8440, 0, -7160, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1F09)

    Sleep(200)

    @scena.Lambda('lambda_1F29')
    def lambda_1F29():
        ChrWalkTo(0x00FE, 7090, 0, -7730, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1F29)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0101, 0)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetChipByIndex(0x0107, 20)
    ChrSetSubChip(0x0107, 0)
    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1F7F'),
        (0x00000003, 'loc_1F87'),
        (0x00000004, 'loc_1F8F'),
        (0x00000007, 'loc_1F97'),
        (-1, 'loc_1F9F'),
    )

    def _loc_1F7F(): pass

    label('loc_1F7F')

    ChrSetChipByIndex(0x00F9, 8)

    Jump('loc_1F9F')

    def _loc_1F87(): pass

    label('loc_1F87')

    ChrSetChipByIndex(0x00F9, 11)

    Jump('loc_1F9F')

    def _loc_1F8F(): pass

    label('loc_1F8F')

    ChrSetChipByIndex(0x00F9, 14)

    Jump('loc_1F9F')

    def _loc_1F97(): pass

    label('loc_1F97')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_1F9F')

    def _loc_1F9F(): pass

    label('loc_1F9F')

    ChrTalk(
        0x0101,
        (
            '#0010311029V#1005F#5P阿加特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311030V#054F#2P虽然已经出现裂痕了，\n',
            '但是还不到破坏的地步！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311031V既然如此，\n',
            '只好再制造一次机会了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311032V帮我个忙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311033V#1006F#5P当然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230806V#062F#5P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20C2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311035V#024F#5P……上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_215E')

    def _loc_20C2(): pass

    label('loc_20C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20F7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311036V#046F#5P……上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_215E')

    def _loc_20F7(): pass

    label('loc_20F7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_212C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311037V#530F#5P……上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_215E')

    def _loc_212C(): pass

    label('loc_212C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_215E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311038V#076F#5P……上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_215E(): pass

    label('loc_215E')

    Fade(500)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 125)
    OP_70(0x0000, 180)
    Sleep(1300)

    @scena.Lambda('lambda_2181')
    def lambda_2181():
        CameraSetDistance(1500, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2181)

    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    Sleep(800)

    FadeIn(0, 0)
    OP_0D()
    TerminateThread(0x0101, 0x02)
    OP_23(0x0090)
    Battle(0x0000044F, 0x00000000, 0x00, 0x0080, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_21E1'),
        (-1, 'loc_21E6'),
    )

    def _loc_21E1(): pass

    label('loc_21E1')

    OP_B4(0x00)

    Jump('loc_21E6')

    def _loc_21E6(): pass

    label('loc_21E6')

    OP_20(0x00000000)

    Return()

# id: 0x0006 offset: 0x21EC
@scena.Code('func_06_21EC')
def func_06_21EC():
    ChrClearFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 24)
    ChrJumpTo(0x0106, 3860, 0, -4770, 500, 6000)
    ChrSetDirection(0x0106, 0, 0)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 2)
    ChrSetChipByIndex(0x0106, 28)

    Return()

# id: 0x0007 offset: 0x2229
@scena.Code('func_07_2229')
def func_07_2229():
    ChrClearFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 24)
    ChrJumpTo(0x0106, 9360, 0, -4990, 500, 6000)
    ChrSetDirection(0x0106, 0, 0)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 2)
    ChrSetChipByIndex(0x0106, 28)

    Return()

# id: 0x0008 offset: 0x2266
@scena.Code('func_08_2266')
def func_08_2266():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    CameraMove(9500, 9450, 12390, 0)
    OP_67(0, 5510, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(346000, 0)
    OP_6E(510, 0)
    OP_71(0x0001, 0x0004)
    ChrSetPos(0x0106, 4950, 0, -2860, 0)
    ChrSetPos(0x0101, 3900, 0, -3700, 0)
    ChrSetPos(0x0107, 5990, 0, -3790, 0)
    ChrSetPos(0x00F9, 5500, 0, -4500, 0)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 3)
    ChrSetChipByIndex(0x0106, 28)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0107, 20)
    ChrSetSubChip(0x0107, 0)
    ChrSetSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_233A'),
        (0x00000003, 'loc_2342'),
        (0x00000004, 'loc_234A'),
        (0x00000007, 'loc_2352'),
        (-1, 'loc_235A'),
    )

    def _loc_233A(): pass

    label('loc_233A')

    ChrSetChipByIndex(0x00F9, 8)

    Jump('loc_235A')

    def _loc_2342(): pass

    label('loc_2342')

    ChrSetChipByIndex(0x00F9, 11)

    Jump('loc_235A')

    def _loc_234A(): pass

    label('loc_234A')

    ChrSetChipByIndex(0x00F9, 14)

    Jump('loc_235A')

    def _loc_2352(): pass

    label('loc_2352')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_235A')

    def _loc_235A(): pass

    label('loc_235A')

    OP_A1(0x000A, 0x0000)
    ChrSetPos(0x000A, 10000, 300, 14130, 192)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 630)
    OP_70(0x0000, 640)
    ChrSetDirection(0x000B, 180, 0)
    OP_CF(0x000B, 0x00, 'Frame127_FireEmitter')
    ChrSetFlags(0x000A, 0x0001)
    ChrClearFlags(0x000A, 0x0080)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x07,
        (
            (Expr.PushLong, 0x1964),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(2000, 0)
    CreateThread(0x000A, 0x00, 0x00, func_19_6BE4)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 640)
    OP_70(0x0000, 670)
    Sleep(3000)

    Fade(500)
    CameraMove(4300, 0, -3270, 0)
    OP_67(0, 7030, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_2453')
    def lambda_2453():
        CameraMove(4300, 0, -4270, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2453)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24BD',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_24F1')

    def _loc_24BD(): pass

    label('loc_24BD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24DF',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_24F1')

    def _loc_24DF(): pass

    label('loc_24DF')

    OP_62(0x00F9, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_24F1(): pass

    label('loc_24F1')

    CreateThread(0x00F9, 0x01, 0x00, func_12_6337)
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x00, func_0F_62B2)
    Sleep(50)

    CreateThread(0x0107, 0x01, 0x00, func_11_630E)
    Sleep(100)

    CreateThread(0x0106, 0x01, 0x00, func_10_62DB)
    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070311039V#065F#6P啊、啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311040V#1005F#6P呜……\n',
            '应该打倒了才对啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25CA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311041V#523F#6P无限的生命力……\n',
            '和传说一样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A3')

    def _loc_25CA(): pass

    label('loc_25CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2612',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311042V#042F#6P无限的生命力……\n',
            '和传说一样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A3')

    def _loc_2612(): pass

    label('loc_2612')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_265C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311043V#039F#6P无限的生命力……\n',
            '和传说一样吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A3')

    def _loc_265C(): pass

    label('loc_265C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311044V#077F#6P无限的生命力……\n',
            '和传说一样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A3(): pass

    label('loc_26A3')

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_26C5')
    def lambda_26C5():
        CameraMove(3260, 8370, -1910, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26C5)

    @scena.Lambda('lambda_26DD')
    def lambda_26DD():
        OP_67(0, 2800, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_26DD)

    @scena.Lambda('lambda_26F5')
    def lambda_26F5():
        CameraSetDistance(3400, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26F5)

    @scena.Lambda('lambda_2705')
    def lambda_2705():
        OP_6C(315000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2705)

    @scena.Lambda('lambda_2715')
    def lambda_2715():
        OP_6E(342, 2500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2715)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1500)

    Fade(500)
    CameraMove(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311045V#054F#5P提妲！\n',
            '你带了闪光弹吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070311046V#064F#6P呜哎……带了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2861',
    )

    ChrTalk(
        0x0106,
        (
            '#0050311047V#054F#5P用那个扰乱龙的视线！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311048V艾丝蒂尔，雪拉扎德！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311049V别让他动，哪怕一下子也行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29F3')

    def _loc_2861(): pass

    label('loc_2861')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28EA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050311047V#054F#5P用那个扰乱龙的视线！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311051V艾丝蒂尔，公主殿下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311049V别让他动，哪怕一下子也行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29F3')

    def _loc_28EA(): pass

    label('loc_28EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2973',
    )

    ChrTalk(
        0x0106,
        (
            '#0050311047V#054F#5P用那个扰乱龙的视线！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311054V艾丝蒂尔，奥利维尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311049V别让他动，哪怕一下子也行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29F3')

    def _loc_2973(): pass

    label('loc_2973')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29F3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050311047V#054F#5P用那个扰乱龙的视线！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311057V艾丝蒂尔，金！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311049V别让他动，哪怕一下子也行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29F3(): pass

    label('loc_29F3')

    ChrTalk(
        0x0101,
        (
            '#0010311059V#1020F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 23)
    ChrSetSubChip(0x0106, 0)
    OP_21()
    PlayBGM(43)
    Sleep(500)

    @scena.Lambda('lambda_2A3D')
    def lambda_2A3D():
        OP_69(0x00FE, 1500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2A3D)

    OP_67(0, 4500, -10000, 1500)
    OP_C4(0x00, 0x00000040)
    OP_6A(0x0106)

    @scena.Lambda('lambda_2A65')
    def lambda_2A65():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_2A65')

    DispatchAsync2(0x0101, 0x0001, lambda_2A65)

    @scena.Lambda('lambda_2A76')
    def lambda_2A76():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_2A76')

    DispatchAsync2(0x0107, 0x0001, lambda_2A76)

    @scena.Lambda('lambda_2A87')
    def lambda_2A87():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_2A87')

    DispatchAsync2(0x00F9, 0x0001, lambda_2A87)

    ChrClearFlags(0x0106, 0x0002)
    ChrClearFlags(0x0106, 0x0020)
    ChrClearFlags(0x0106, 0x0010)
    ChrSetFlags(0x0106, 0x0004)
    ChrSetFlags(0x0106, 0x0020)
    ChrSetFlags(0x0106, 0x1000)
    Sleep(500)

    CreateThread(0x0106, 0x00, 0x00, func_0D_615E)
    ChrWalkTo(0x0106, -3890, 0, -370, 10000, 0x00)
    TerminateThread(0x0106, 0x00)
    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0106, 2)
    ChrJumpTo(0x0106, -5070, 2000, 1340, 2500, 10000)
    ChrSetSubChip(0x0106, 3)
    PlaySE(164, 0x00, 0x64)
    ChrSetDirection(0x0106, 270, 0)
    ChrSetSubChip(0x0106, 4)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0106, 6)
    ChrJumpTo(0x0106, -8720, 4000, 1580, 2500, 10000)
    ChrSetSubChip(0x0106, 7)
    PlaySE(164, 0x00, 0x64)
    ChrSetDirection(0x0106, 0, 0)
    ChrSetSubChip(0x0106, 6)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0106, 2)
    ChrJumpTo(0x0106, -10600, 6000, 4370, 2500, 10000)
    ChrSetSubChip(0x0106, 3)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    ChrSetSubChip(0x0106, 4)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0106, 6)
    ChrJumpTo(0x0106, -11870, 8000, 7650, 2500, 10000)
    ChrSetSubChip(0x0106, 7)
    PlaySE(164, 0x00, 0x64)
    ChrSetDirection(0x0106, 90, 0)
    ChrSetSubChip(0x0106, 0)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0106, 2)
    ChrJumpTo(0x0106, -6820, 10000, 7900, 2500, 10000)
    ChrSetSubChip(0x0106, 3)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    ChrSetChipByIndex(0x0106, 23)
    ChrSetSubChip(0x0106, 0)
    ChrClearFlags(0x0106, 0x0020)
    Sleep(200)

    OP_6A(0x00FF)
    OP_C4(0x01, 0x00000040)

    @scena.Lambda('lambda_2C15')
    def lambda_2C15():
        CameraSetDistance(2800, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C15)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 8)
    ChrSetChipByIndex(0x0106, 32)
    OP_0D()
    Sleep(300)

    PlaySE(157, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_2C4E')
    def lambda_2C4E():
        OP_99(0x00FE, 0x09, 0x0F, 1500)
        Yield()

        Jump('lambda_2C4E')

    DispatchAsync2(0x0106, 0x0002, lambda_2C4E)

    Sleep(1000)

    Fade(500)
    CameraMove(4300, 0, -4270, 0)
    OP_67(0, 7030, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070311060V#560F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D11',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311061V#020F#6P原来如此……\n',
            '是这样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC4')

    def _loc_2D11(): pass

    label('loc_2D11')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D53',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311062V#040F#6P原来如此……\n',
            '是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC4')

    def _loc_2D53(): pass

    label('loc_2D53')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D8E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311063V#030F#6P呼……是这样吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC4')

    def _loc_2D8E(): pass

    label('loc_2D8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DC4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311064V#070F#6P……是这样吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC4(): pass

    label('loc_2DC4')

    ChrTurnDirection(0x0101, 0x0107, 500)

    ChrTalk(
        0x0101,
        (
            '#0010311065V#1005F#5P提妲！\n',
            '往高打，别打中！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311066V我们去阻止住它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070311067V#062F#4P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'Scraft\\\\sc003_12.eff')
    LoadEffect(0x02, 'battle\\\\btgun60.eff')
    ChrSetDirection(0x0107, 0, 400)
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x00F9, 0, 400)
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0107, 22)
    ChrSetSubChip(0x0107, 1)
    OP_0D()
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0003)
    PlayEffect(0x02, 0xFF, 0x0107, 0, 500, 500, 0, -45, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2EE0')
    def lambda_2EE0():
        OP_99(0x0107, 0x01, 0x0D, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_2EE0)

    PlayEffect(0x01, 0xFF, 0x00FF, 5990, 11000, -2000, 0, -70, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Fade(500)
    CameraMove(7850, 19290, 3840, 0)
    OP_67(0, 8119, -10000, 0)
    CameraSetDistance(1530, 0)
    OP_6C(315000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(200)

    LoadEffect(0x03, 'map\\\\mp080_00.eff')
    PlayEffect(0x03, 0x01, 0x00FF, 7490, 22750, 4000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(301, 0x00, 0x64)
    Sleep(1000)

    StopEffect(0x01, 0x02)
    PlaySE(405, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    Sleep(2000)

    Fade(500)
    CameraMove(4140, 0, -4630, 0)
    OP_67(0, 6120, -10000, 0)
    CameraSetDistance(3310, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010311068V#1002F#5P（……就是现在！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    @scena.Lambda('lambda_306E')
    def lambda_306E():
        CameraMove(6170, 3860, 9530, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_306E)

    @scena.Lambda('lambda_3086')
    def lambda_3086():
        OP_67(0, 5160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3086)

    @scena.Lambda('lambda_309E')
    def lambda_309E():
        CameraSetDistance(3200, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_309E)

    @scena.Lambda('lambda_30AE')
    def lambda_30AE():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_30AE)

    @scena.Lambda('lambda_30BE')
    def lambda_30BE():
        OP_6E(447, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_30BE)

    LoadEffect(0x01, 'scraft\\\\sc000_11.eff')
    CreateThread(0x0101, 0x01, 0x00, func_13_63C3)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_30FF'),
        (0x00000003, 'loc_3109'),
        (0x00000004, 'loc_3128'),
        (0x00000007, 'loc_3132'),
        (-1, 'loc_313C'),
    )

    def _loc_30FF(): pass

    label('loc_30FF')

    CreateThread(0x00F9, 0x01, 0x00, func_15_669E)

    Jump('loc_313C')

    def _loc_3109(): pass

    label('loc_3109')

    LoadEffect(0x03, 'battle\\btgun00.eff')
    CreateThread(0x00F9, 0x01, 0x00, func_14_64F0)

    Jump('loc_313C')

    def _loc_3128(): pass

    label('loc_3128')

    CreateThread(0x00F9, 0x01, 0x00, func_16_67CC)

    Jump('loc_313C')

    def _loc_3132(): pass

    label('loc_3132')

    CreateThread(0x00F9, 0x01, 0x00, func_17_6985)

    Jump('loc_313C')

    def _loc_313C(): pass

    label('loc_313C')

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_314C')
    def lambda_314C():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_314C')

    DispatchAsync2(0x0101, 0x0003, lambda_314C)

    @scena.Lambda('lambda_315D')
    def lambda_315D():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_315D')

    DispatchAsync2(0x00F9, 0x0003, lambda_315D)

    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetFlags(0x0107, 0x0080)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        CameraMove(3460, 0, 11500, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3178)

    @scena.Lambda('lambda_3190')
    def lambda_3190():
        OP_67(0, 3840, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3190)

    @scena.Lambda('lambda_31A8')
    def lambda_31A8():
        CameraSetDistance(5090, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_31A8)

    @scena.Lambda('lambda_31B8')
    def lambda_31B8():
        OP_6C(327000, 2500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_31B8)

    @scena.Lambda('lambda_31C8')
    def lambda_31C8():
        OP_6E(358, 2500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_31C8)

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 675)
    OP_70(0x0000, 715)
    Sleep(1000)

    PlaySE(136, 0x00, 0x64)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(3240, 0, 860, 0)
    OP_67(0, 4340, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(3000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)

    Fade(500)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x00F9, 0x03)
    ChrSetPos(0x0101, -3310, 0, -12120, 0)
    ChrSetPos(0x0107, -1730, 0, -13800, 0)
    ChrSetPos(0x00F9, -2970, 0, -14040, 0)
    CameraMove(-6970, 10090, 7890, 0)
    OP_67(0, 3200, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0106, 0x02)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 27)
    OP_C4(0x00, 0x00000040)
    OP_69(0x0106, 0)
    OP_6A(0x0106)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311069V#053F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_332D')
    def lambda_332D():
        CameraSetDistance(3200, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_332D)

    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 8)
    ChrSetChipByIndex(0x0106, 32)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050311070V#054F#5S呜哦哦哦哦哦哦哦！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    Fade(250)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 8)
    ChrSetChipByIndex(0x0106, 32)

    @scena.Lambda('lambda_33AF')
    def lambda_33AF():
        OP_99(0x00FE, 0x09, 0x0F, 2000)
        Yield()

        Jump('lambda_33AF')

    DispatchAsync2(0x0106, 0x0002, lambda_33AF)

    Sleep(300)

    LoadEffect(0x01, 'map\\\\mp009_00.eff')
    LoadEffect(0x02, 'map\\\\mp081_00.eff')
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0106, 0x02)
    ChrSetFlags(0x0106, 0x0004)

    @scena.Lambda('lambda_3406')
    def lambda_3406():
        OP_6C(0, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3406)

    ChrSetSubChip(0x0106, 17)
    Sleep(200)

    ChrSetSubChip(0x0106, 18)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_342A')
    def lambda_342A():
        ChrJumpTo(0x0106, 2650, 1600, -3300, 1500, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_342A)

    Sleep(500)

    Fade(500)
    CameraMove(840, 0, -2170, 0)
    OP_67(0, 20860, -10000, 0)
    OP_6C(327000, 0)
    CameraSetDistance(890, 0)
    OP_6E(503, 0)

    @scena.Lambda('lambda_348F')
    def lambda_348F():
        CameraMove(2000, 0, -2900, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_348F)

    @scena.Lambda('lambda_34A7')
    def lambda_34A7():
        CameraSetDistance(630, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_34A7)

    ChrSetSubChip(0x0106, 19)
    ChrSetFlags(0x0106, 0x0800)
    WaitForThreadExit(0x0106, 0x0000)
    WaitForThreadExit(0x0106, 0x0001)
    OP_6A(0x00FF)
    OP_C4(0x01, 0x00000040)
    OP_7C(0, 500, 3000, 500)
    OP_20(0x00000000)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 3000, 1700, -3000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0xFF, 0x00FF, 2650, 1600, -3300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_75(0x00, 0x0000000C, 0x07)
    PlaySE(616, 0x00, 0x64)
    Sleep(300)

    Sleep(1000)

    OP_6F(0x0000, 720)
    OP_70(0x0000, 810)
    PlaySE(405, 0x00, 0x64)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 25)
    ChrSetSubChip(0x0106, 6)
    ChrSetDirection(0x0106, 45, 0)
    ChrSetFlags(0x0106, 0x0800)
    ChrSetFlags(0x0106, 0x0020)
    StopEffect(0x00, 0x02)

    @scena.Lambda('lambda_35AA')
    def lambda_35AA():
        ChrJumpTo(0x0106, 880, 0, -7240, 500, 6000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_35AA)

    @scena.Lambda('lambda_35C8')
    def lambda_35C8():
        OP_99(0x00FE, 0x05, 0x00, 2500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_35C8)

    WaitForThreadExit(0x0106, 0x0000)
    PlaySE(164, 0x00, 0x64)
    ChrMoveToRelativeAsync(0x0106, 0, 0, -2000, 4000, 0x00)
    WaitForThreadExit(0x0106, 0x0001)
    ChrSetChipByIndex(0x0106, 26)

    @scena.Lambda('lambda_3600')
    def lambda_3600():
        OP_99(0x00FE, 0x00, 0x03, 2500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3600)

    Sleep(500)

    Fade(500)
    MapSetFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(5300, 0, 8070, 0)
    OP_67(0, 7510, -10000, 0)
    CameraSetDistance(3680, 0)
    OP_6C(341000, 0)
    OP_6E(435, 0)
    ChrClearFlags(0x0106, 0x0800)
    Sleep(2500)

    PlaySE(136, 0x00, 0x64)
    Sleep(1000)

    PlaySE(403, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(300)

    Fade(500)
    CameraMove(-2870, 0, -12330, 0)
    OP_67(0, 6010, -10000, 0)
    CameraSetDistance(2490, 0)
    OP_6C(336000, 0)
    OP_6E(329, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0107, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0107, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrClearFlags(0x0107, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)
    OP_0D()
    OP_75(0x00, 0x0000000D, 0x07)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010311071V#1008F成功了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3759',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311072V#021F#6P『福音』坏了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3807')

    def _loc_3759(): pass

    label('loc_3759')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3796',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311073V#542F#6P『福音』坏了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3807')

    def _loc_3796(): pass

    label('loc_3796')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37D2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311074V#030F『福音』坏了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3807')

    def _loc_37D2(): pass

    label('loc_37D2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3807',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311075V#070F『福音』坏了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3807(): pass

    label('loc_3807')

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070311076V#065F#6P阿加特哥哥！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlayBGM(1)
    Sleep(300)

    @scena.Lambda('lambda_3855')
    def lambda_3855():
        ChrWalkTo(0x00FE, 580, 0, -10500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3855)

    Sleep(300)

    @scena.Lambda('lambda_3875')
    def lambda_3875():
        ChrWalkTo(0x00FE, -710, 0, -8400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3875)

    @scena.Lambda('lambda_3890')
    def lambda_3890():
        CameraMove(-330, 0, -7100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3890)

    @scena.Lambda('lambda_38A8')
    def lambda_38A8():
        OP_67(0, 5350, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38A8)

    @scena.Lambda('lambda_38C0')
    def lambda_38C0():
        OP_6C(348000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_38C0)

    Sleep(100)

    @scena.Lambda('lambda_38D5')
    def lambda_38D5():
        ChrWalkTo(0x00FE, -740, 0, -10400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_38D5)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_38F5')
    def lambda_38F5():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_38F5)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_3908')
    def lambda_3908():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3908)

    WaitForThreadExit(0x00F9, 0x0001)
    ChrTurnDirection(0x00F9, 0x0106, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0107,
        (
            '#0070311077V#065F#6P阿加特哥哥！\n',
            '不要紧吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311078V#053F#5P啊啊……没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0106, 0x03, 0x00, 1500)
    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0106, 0x0800)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetSubChip(0x0106, 0)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0106, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311079V#051F#2P看来……\n',
            '好像很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311080V#1001F#5P嗯嗯！　很成功哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A59',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311081V#021F#6P呵呵，不是被你抢走\n',
            '风头了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B16')

    def _loc_3A59(): pass

    label('loc_3A59')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A98',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311082V#041F#6P阿加特……太厉害了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B16')

    def _loc_3A98(): pass

    label('loc_3A98')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3ADE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311083V#031F#6P哎呀哎呀，\n',
            '风头都被抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B16')

    def _loc_3ADE(): pass

    label('loc_3ADE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B16',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311084V#071F#6P哈哈，真了不起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B16(): pass

    label('loc_3B16')

    ChrTalk(
        0x0106,
        (
            '#0050311085V#051F#2P嘿嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311086V龙也总算被打倒了，\n',
            '该说是告一段落吧──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311087V…………漂亮………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C2E',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3C6C')

    def _loc_3C2E(): pass

    label('loc_3C2E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C55',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3C6C')

    def _loc_3C55(): pass

    label('loc_3C55')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3C6C(): pass

    label('loc_3C6C')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010311088V#1020F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311089V#065F刚、刚才的声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311090V#055F#2P哪里传来的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D1C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311091V#024F#6P难不成……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DBC')

    def _loc_3D1C(): pass

    label('loc_3D1C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D55',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311092V#043F#6P难、难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DBC')

    def _loc_3D55(): pass

    label('loc_3D55')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D8A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311093V#033F#6P哦哦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DBC')

    def _loc_3D8A(): pass

    label('loc_3D8A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DBC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311094V#073F#6P哦哦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DBC(): pass

    label('loc_3DBC')

    CreateThread(0x000A, 0x00, 0x00, func_0C_610A)

    @scena.Lambda('lambda_3DC9')
    def lambda_3DC9():
        CameraMove(1620, 4000, -2120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3DC9)

    @scena.Lambda('lambda_3DE1')
    def lambda_3DE1():
        OP_67(0, 1110, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3DE1)

    @scena.Lambda('lambda_3DF9')
    def lambda_3DF9():
        OP_6C(359000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3DF9)

    @scena.Lambda('lambda_3E09')
    def lambda_3E09():
        CameraSetDistance(2950, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_3E09)

    @scena.Lambda('lambda_3E19')
    def lambda_3E19():
        OP_6E(603, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_3E19)

    OP_6F(0x0000, 815)
    OP_70(0x0000, 865)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 870)
    OP_70(0x0000, 920)
    WaitForThreadExit(0x0106, 0x0003)
    Sleep(500)

    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311095V干得漂亮……人类之子们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311096V我名叫『雷格纳特』。\n',
            '我是长眠于此的龙之眷族。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311097V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311098V#052F#5P这是……\n',
            '你会说话吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311099V我并没有像你们\n',
            '一样的发声器官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311100V所以只能用“意念”\n',
            '的方式来同你们讲话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311101V你们就用平常的方式\n',
            '出声同我交谈就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0106,
        (
            '#0050311102V#055F#5P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311103V#064F#5P呜哎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311104V#1015F#5P既、既然可以沟通的话，\n',
            '我想确认一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311105V你不会再想\n',
            '和我们战斗了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311106V嗯，我只是\n',
            '被那机械操纵了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311107V你们干得很好，竟能把我\n',
            '从束缚中解放出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311108V请接受我诚挚的谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311109V#1016F#5P啊哈哈……\n',
            '不、不客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311110V#053F#5P呼……道谢就不必了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311111V#057F我们来这里\n',
            '并不是为了解放你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311112V而是为了避免你造成更大的破坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311113V你是说被我攻击的\n',
            '那些城镇和村子吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311114V虽说这并非是我有意而为，\n',
            '但我本身的确也有不可推卸的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311115V那么……该如何补偿才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311116V#1025F#5P嗯、不过，反正是\n',
            '『结社』的人不好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311117V虽然出现了伤者，\n',
            '但却没有任何人牺牲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311118V#1016F只要表达出诚意\n',
            '应该可以原谅你哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311119V#552F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311120V唔，诚意吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311121V这种东西是否能表达\n',
            '其实没什么自信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311122V来，人类的孩子，\n',
            '再稍微靠近这边一点可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311123V#1004F#5P唔、嗯？\n',
            '倒是没什么不可以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311124V#555F#5P……真是的，在说什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_44D0')
    def lambda_44D0():
        CameraMove(2860, 3050, 3590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44D0)

    @scena.Lambda('lambda_44E8')
    def lambda_44E8():
        OP_67(0, 3540, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44E8)

    @scena.Lambda('lambda_4500')
    def lambda_4500():
        OP_6C(347000, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_4500)

    @scena.Lambda('lambda_4510')
    def lambda_4510():
        OP_6E(596, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_4510)

    @scena.Lambda('lambda_4520')
    def lambda_4520():
        CameraSetDistance(2970, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_4520)

    @scena.Lambda('lambda_4530')
    def lambda_4530():
        ChrWalkTo(0x00FE, 860, 0, -2700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4530)

    Sleep(100)

    ChrClearFlags(0x0106, 0x1000)
    ChrClearFlags(0x0106, 0x0020)

    @scena.Lambda('lambda_455A')
    def lambda_455A():
        ChrWalkTo(0x00FE, 2240, 0, -2990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_455A)

    Sleep(100)

    @scena.Lambda('lambda_457A')
    def lambda_457A():
        ChrWalkTo(0x00FE, 1890, 0, -4200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_457A)

    Sleep(100)

    @scena.Lambda('lambda_459A')
    def lambda_459A():
        ChrWalkTo(0x00FE, 510, 0, -3910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_459A)

    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(300)

    LoadEffect(0x00, 'map\\\\mp075_00.eff')
    Sleep(100)

    ChrSetPos(0x000C, 1100, 9000, -2550, 0)
    ChrSetPos(0x000D, 2420, 9000, -2650, 0)
    PlayEffect(0x00, 0x01, 0x000C, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x000D, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(137, 0x00, 0x64)
    Sleep(2000)

    @scena.Lambda('lambda_4673')
    def lambda_4673():
        ChrMoveToRelativeAsync(0x00FE, 0, -8200, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4673)

    @scena.Lambda('lambda_468E')
    def lambda_468E():
        ChrMoveToRelativeAsync(0x00FE, 0, -8000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_468E)

    Sleep(1000)

    Fade(500)
    CameraMove(2180, 0, -4750, 0)
    OP_67(0, 7100, -10000, 0)
    CameraSetDistance(1240, 0)
    OP_6C(166000, 0)
    OP_6E(611, 0)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 33)
    ChrSetSubChip(0x0101, 15)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 7)
    OP_0D()
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    ChrSetPos(0x000E, 1150, 0, -2550, 0)
    ChrSetPos(0x000F, 2500, 130, -2650, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    Sleep(1000)

    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    OP_23(0x0089)

    ChrTalk(
        0x0106,
        (
            '#0050311125V#052F#5P什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311126V#560F#5P哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311127V#1004F#5P这是……\n',
            '七耀石的结晶！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4829',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311128V#023F#2P金色的光辉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030311129V蕴藏了空之力的\n',
            '金耀石结晶对吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4956')

    def _loc_4829(): pass

    label('loc_4829')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_488F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311130V#044F#2P金色的光辉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060311131V蕴藏了空之力的\n',
            '金耀石结晶对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4956')

    def _loc_488F(): pass

    label('loc_488F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48F5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311132V#033F#2P金色的光辉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311133V蕴藏了空之力的\n',
            '金耀石结晶吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4956')

    def _loc_48F5(): pass

    label('loc_48F5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4956',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311134V#073F#2P金色的光辉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080311135V蕴藏了空之力的\n',
            '金耀石结晶吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4956(): pass

    label('loc_4956')

    SetMessageWindowPos(50, 75, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311136V这就算是我对自己犯下的过错而作的一点补偿吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311137V可以请你们帮忙\n',
            '交给城镇和村中之长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)

    Fade(500)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetSubChip(0x0106, 0)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010311138V#1008F#5P原、原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311139V#1006F嗯，这样的话──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311140V#053F#5P──不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010311141V#1019F#6P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311142V#063F#5P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311143V唔，难道是这东西\n',
            '还不足够表达我的诚意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0106,
        (
            '#0050311144V#053F#5P不是这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311145V#050F按这块结晶的大小来看……\n',
            '估计一个价值1千万米拉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311146V再给我们一快相同的结晶吧，\n',
            '是这块的一万分之一就可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311147V#1004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311148V#051F#5P如果是和犯罪无关的事情，\n',
            '雇用游击士是要收费的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311149V比如物品的搬运费，\n',
            '收个１０００米拉就够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311150V只要你付了这笔钱，我们就帮你带这块结晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311151V#560F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311152V#1007F#6P真受不了……\n',
            '真是死板的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 75, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311153V唔，原来是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311154V那么就收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(2860, 3050, 3590, 0)
    OP_67(0, 3540, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(347000, 0)
    OP_6E(596, 0)
    OP_0D()
    ChrSetPos(0x000C, 2420, 9000, -2650, 0)
    PlayEffect(0x00, 0x00, 0x000C, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlaySE(137, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_4E43')
    def lambda_4E43():
        ChrMoveToRelativeAsync(0x00FE, 0, -8000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_4E43)

    Sleep(500)

    ChrSetFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 3)
    WaitForThreadExit(0x000C, 0x0003)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 33)
    ChrSetSubChip(0x000F, 17)
    ChrSetPos(0x000F, 2500, 200, -2650, 0)
    Sleep(500)

    StopEffect(0x00, 0x02)
    OP_23(0x0089)
    Sleep(300)

    Fade(500)
    ChrClearFlags(0x0106, 0x0002)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetSubChip(0x0106, 0)
    ChrSetFlags(0x000F, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311155V#051F#5P好……成交。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311156V这两样东西，我们会负责\n',
            '送交给村长和市长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311157V唔，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311158V呵呵……话说回来，\n',
            '刚才的那一击真是相当不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311159V当初与银发剑士作战的时候，\n',
            '还根本派不上什么用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311160V士别三日、刮目相看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_501F')
    def lambda_501F():
        ChrSetDirection(0x00FE, 25, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_501F)

    ChrTalk(
        0x0106,
        (
            '#0050311161V#055F#5P什…什么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311162V#064F#5P废、废坑的事\n',
            '你还记着吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(2710, 5820, 8720, 0)
    OP_67(0, 880, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(355000, 0)
    OP_6E(596, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311163V虽然我被操纵了，\n',
            '但还保留着意识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311164V小姑娘啊。\n',
            '你的勇气和活泼\n',
            '相当令人钦佩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311165V呵呵……\n',
            '所以说人类真是有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0107,
        (
            '#0070311166V#562F#5P啊，啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311167V#1016F#5P啊哈哈，\n',
            '你还挺会开玩笑的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311168V唔，还有你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311169V原来如此，难怪\n',
            '气味很熟悉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311170V你是『剑圣』的女儿吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311171V#1004F#3S#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_52E0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311172V#023F#5P为、为什么\n',
            '你会知道老师的事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536D')

    def _loc_52E0(): pass

    label('loc_52E0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5338',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311173V#073F#5P这可真令人吃惊……\n',
            '你怎么知道卡西乌斯大人的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536D')

    def _loc_5338(): pass

    label('loc_5338')

    ChrTalk(
        0x0106,
        (
            '#0050311174V#055F#5P喂喂，为什么\n',
            '认识大叔啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_536D(): pass

    label('loc_536D')

    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311175V他是２０年前，我开始沉睡之前，\n',
            '最后遇见的人类之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311176V自称要追求剑之道的极至\n',
            '而鲁莽地向我挑战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311177V他现在还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311178V#1015F#5P嗯、嗯……\n',
            '依旧还是生龙活虎的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311179V#1019F……只是没想到\n',
            '居然连龙都认识啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54E4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311180V#045F#5P呵呵……\n',
            '不愧是卡西乌斯先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5560')

    def _loc_54E4(): pass

    label('loc_54E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_552E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311181V#031F#5P呵呵，不愧是\n',
            '卡西乌斯·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5560')

    def _loc_552E(): pass

    label('loc_552E')

    ChrTalk(
        0x0106,
        (
            '#0050311182V#551F#5P真是个不得了的大叔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5560(): pass

    label('loc_5560')

    ChrTalk(
        0x0101,
        (
            '#0010311183V#1004F#5P啊，这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311184V#1002F对了，『雷格纳特』。\n',
            '可以问你件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311185V唔，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311186V#1002F#5P在你身上装置『福音』的人，\n',
            '就是那个叫莱维的男子吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311187V他曾经说过『实验』什么的……\n',
            '你知道究竟是什么实验吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311188V#5P唔……我要解释一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311189V将漆黑的机关装在我身上的\n',
            '不是那个银发剑士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311190V是一位被称为教授，\n',
            '拥有神秘力量的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311191V#1005F#5P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311192V#052F#5P居然……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311193V银发剑士是陪伴着教授\n',
            '一同出现在这里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311194V而在我失控之后，\n',
            '他用尽了各种手段，\n',
            '力图避免我造成更大的破坏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311195V如果不是有他的阻止，\n',
            '我想我一定会将整个城镇和村子\n',
            '都破坏殆尽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311196V#1026F#5P不、不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311197V#552F#5P这家伙……到底想干什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311198V而『教授』的目的只有一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311199V就是看那个机关是否对我有效，\n',
            '以此来确认作为『辉之环』的『福音』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311200V的完成度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0106,
        (
            '#0050311201V#054F#5P什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311202V#065F#5P啊、『辉之环』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310663V#1020F#5P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010311204V莫非你知道『辉之环』\n',
            '是什么东西！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311205V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311206V那是无所存在，\n',
            '却又无处不在的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311207V它的存在赋予了人们无限的力量和睿智。\n',
            '同时，也赋予了人们无尽的绝望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311208V当其迫近在眼前的时候……\n',
            '人们必须要作出一个回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010311209V#1004F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BB2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030311210V#022F#5P那是……\n',
            '什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C71')

    def _loc_5BB2(): pass

    label('loc_5BB2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BF2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060311211V#043F#5P那是……\n',
            '什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C71')

    def _loc_5BF2(): pass

    label('loc_5BF2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C34',
    )

    ChrTalk(
        0x0104,
        (
            '#0040311212V#032F#5P唔……\n',
            '那是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C71')

    def _loc_5C34(): pass

    label('loc_5C34')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C71',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311213V#072F#5P唔……\n',
            '那是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C71(): pass

    label('loc_5C71')

    SetMessageWindowPos(320, 200, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311214V我能说的只有这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311215V过多的干预，\n',
            '是古代的盟约所禁止的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311216V所以我不能帮助你们，\n',
            '也不能阻止他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(990, 9040, 6400, 0)
    OP_67(0, 9540, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(302000, 0)
    OP_6E(537, 0)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_A1(0x000A, 0x0001)
    OP_75(0x01, 0x0000000D, 0x07)
    OP_75(0x01, 0x0000000C, 0x07)
    ChrSetFlags(0x000A, 0x0001)
    ChrClearFlags(0x000A, 0x0080)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x07,
        (
            (Expr.PushLong, 0x1964),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0001, 225)
    OP_70(0x0001, 275)
    OP_B0(0x0001, 0x0A)
    OP_6F(0x0001, 185)
    OP_70(0x0001, 225)
    Sleep(1000)

    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0001)
    OP_6F(0x0001, 225)
    OP_70(0x0001, 248)
    OP_B0(0x0001, 0x0A)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 235)
    OP_70(0x0001, 248)
    Fade(500)
    CameraMove(4560, 4330, 2550, 0)
    OP_67(0, 1770, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(359000, 0)
    OP_6E(644, 0)
    CreateThread(0x0101, 0x00, 0x00, func_0C_610A)
    CreateThread(0x000A, 0x03, 0x00, func_09_607B)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010290835V#1020F#5P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311218V#052F#5P喂、喂！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    SetMessageWindowPos(320, 175, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490311219V再见了，人类的孩子们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311220V在你们找到答案之时，\n',
            '我或许会再次现身吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490311221V我期待着那一天的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(7520, 0, 15130, 0)
    OP_67(0, 14200, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(340000, 0)
    OP_6E(473, 0)
    TerminateThread(0x000A, 0x03)
    OP_0D()
    CreateThread(0x000A, 0x03, 0x00, func_0A_6097)
    Fade(500)
    OP_72(0x0001, 0x0020)
    OP_73(0x0001)
    OP_D8(0x01, 0x01F4)
    OP_6F(0x0001, 545)
    OP_70(0x0001, 564)

    @scena.Lambda('lambda_5FE2')
    def lambda_5FE2():
        CameraMove(7000, 3000, 21300, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5FE2)

    @scena.Lambda('lambda_5FFA')
    def lambda_5FFA():
        OP_67(0, 18800, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FFA)

    @scena.Lambda('lambda_6012')
    def lambda_6012():
        CameraSetDistance(2810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6012)

    @scena.Lambda('lambda_6022')
    def lambda_6022():
        OP_6C(2000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6022)

    @scena.Lambda('lambda_6032')
    def lambda_6032():
        OP_6E(595, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6032)

    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 565)
    OP_70(0x0001, 585)
    CreateThread(0x0106, 0x00, 0x00, func_0E_6196)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x607B
@scena.Code('func_09_607B')
def func_09_607B():
    Sleep(400)

    def _loc_6080(): pass

    label('loc_6080')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6096',
    )

    PlaySE(288, 0x00, 0x64)
    Sleep(1300)

    Jump('loc_6080')

    def _loc_6096(): pass

    label('loc_6096')

    Return()

# id: 0x000A offset: 0x6097
@scena.Code('func_0A_6097')
def func_0A_6097():
    PlaySE(288, 0x00, 0x64)
    Sleep(2100)

    PlaySE(288, 0x00, 0x64)
    Sleep(2000)

    PlaySE(288, 0x00, 0x64)
    Sleep(2000)

    Return()

# id: 0x000B offset: 0x60B6
@scena.Code('func_0B_60B6')
def func_0B_60B6():
    @scena.Lambda('lambda_60BC')
    def lambda_60BC():
        ChrSetDirection(0x00FE, 0, 400)
        Yield()

        Jump('lambda_60BC')

    DispatchAsync2(0x0106, 0x0001, lambda_60BC)

    Sleep(100)

    @scena.Lambda('lambda_60D2')
    def lambda_60D2():
        ChrSetDirection(0x00FE, 0, 400)
        Yield()

        Jump('lambda_60D2')

    DispatchAsync2(0x0101, 0x0001, lambda_60D2)

    Sleep(100)

    @scena.Lambda('lambda_60E8')
    def lambda_60E8():
        ChrSetDirection(0x00FE, 0, 400)
        Yield()

        Jump('lambda_60E8')

    DispatchAsync2(0x0107, 0x0001, lambda_60E8)

    Sleep(100)

    @scena.Lambda('lambda_60FE')
    def lambda_60FE():
        ChrSetDirection(0x00FE, 0, 400)
        Yield()

        Jump('lambda_60FE')

    DispatchAsync2(0x00F9, 0x0001, lambda_60FE)

    Return()

# id: 0x000C offset: 0x610A
@scena.Code('func_0C_610A')
def func_0C_610A():
    @scena.Lambda('lambda_6110')
    def lambda_6110():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_6110')

    DispatchAsync2(0x0106, 0x0001, lambda_6110)

    Sleep(100)

    @scena.Lambda('lambda_6126')
    def lambda_6126():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_6126')

    DispatchAsync2(0x0101, 0x0001, lambda_6126)

    Sleep(100)

    @scena.Lambda('lambda_613C')
    def lambda_613C():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_613C')

    DispatchAsync2(0x0107, 0x0001, lambda_613C)

    Sleep(100)

    @scena.Lambda('lambda_6152')
    def lambda_6152():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_6152')

    DispatchAsync2(0x00F9, 0x0001, lambda_6152)

    Return()

# id: 0x000D offset: 0x615E
@scena.Code('func_0D_615E')
def func_0D_615E():
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 29)
    OP_99(0x0106, 0x00, 0x07, 2500)
    OP_99(0x0106, 0x00, 0x07, 2500)
    OP_99(0x0106, 0x00, 0x07, 2500)
    OP_99(0x0106, 0x00, 0x07, 2500)
    OP_99(0x0106, 0x00, 0x07, 2500)

    Return()

# id: 0x000E offset: 0x6196
@scena.Code('func_0E_6196')
def func_0E_6196():
    @scena.Lambda('lambda_619C')
    def lambda_619C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_619C)

    Sleep(300)

    @scena.Lambda('lambda_61BC')
    def lambda_61BC():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_61BC)

    Sleep(300)

    @scena.Lambda('lambda_61DC')
    def lambda_61DC():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_61DC)

    Sleep(300)

    @scena.Lambda('lambda_61FC')
    def lambda_61FC():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_61FC)

    Sleep(300)

    @scena.Lambda('lambda_621C')
    def lambda_621C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_621C)

    Sleep(200)

    @scena.Lambda('lambda_623C')
    def lambda_623C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_623C)

    Sleep(200)

    @scena.Lambda('lambda_625C')
    def lambda_625C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_625C)

    Sleep(200)

    @scena.Lambda('lambda_627C')
    def lambda_627C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_627C)

    Sleep(200)

    @scena.Lambda('lambda_629C')
    def lambda_629C():
        ChrMoveToRelativeAsync(0x00FE, 0, 80000, -10000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_629C)

    Return()

# id: 0x000F offset: 0x62B2
@scena.Code('func_0F_62B2')
def func_0F_62B2():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 6)
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -1000, 2000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 5)

    Return()

# id: 0x0010 offset: 0x62DB
@scena.Code('func_10_62DB')
def func_10_62DB():
    ChrClearFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 24)
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -1000, 2000, 0x00)
    ChrSetFlags(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 3)
    ChrSetChipByIndex(0x0106, 28)

    Return()

# id: 0x0011 offset: 0x630E
@scena.Code('func_11_630E')
def func_11_630E():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 21)
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -1000, 2000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 20)

    Return()

# id: 0x0012 offset: 0x6337
@scena.Code('func_12_6337')
def func_12_6337():
    ChrSetSubChip(0x00F9, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_6355'),
        (0x00000003, 'loc_635D'),
        (0x00000004, 'loc_6365'),
        (0x00000007, 'loc_636D'),
        (-1, 'loc_6375'),
    )

    def _loc_6355(): pass

    label('loc_6355')

    ChrSetChipByIndex(0x00F9, 9)

    Jump('loc_6375')

    def _loc_635D(): pass

    label('loc_635D')

    ChrSetChipByIndex(0x00F9, 12)

    Jump('loc_6375')

    def _loc_6365(): pass

    label('loc_6365')

    ChrSetChipByIndex(0x00F9, 15)

    Jump('loc_6375')

    def _loc_636D(): pass

    label('loc_636D')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_6375')

    def _loc_6375(): pass

    label('loc_6375')

    ChrMoveToRelativeAsync(0x00FE, 0, 0, -1500, 2000, 0x00)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_63A2'),
        (0x00000003, 'loc_63AA'),
        (0x00000004, 'loc_63B2'),
        (0x00000007, 'loc_63BA'),
        (-1, 'loc_63C2'),
    )

    def _loc_63A2(): pass

    label('loc_63A2')

    ChrSetChipByIndex(0x00F9, 8)

    Jump('loc_63C2')

    def _loc_63AA(): pass

    label('loc_63AA')

    ChrSetChipByIndex(0x00F9, 11)

    Jump('loc_63C2')

    def _loc_63B2(): pass

    label('loc_63B2')

    ChrSetChipByIndex(0x00F9, 14)

    Jump('loc_63C2')

    def _loc_63BA(): pass

    label('loc_63BA')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_63C2')

    def _loc_63C2(): pass

    label('loc_63C2')

    Return()

# id: 0x0013 offset: 0x63C3
@scena.Code('func_13_63C3')
def func_13_63C3():
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 6)
    ChrWalkTo(0x00FE, 5940, 0, 9270, 10000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_63F6')
    def lambda_63F6():
        ChrJumpTo(0x00FE, 7870, 2500, 14000, 3000, 7000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_63F6)

    Sleep(100)

    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    @scena.Lambda('lambda_6423')
    def lambda_6423():
        OP_99(0x00FE, 0x00, 0x09, 2500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6423)

    Sleep(100)

    PlaySE(500, 0x00, 0x64)
    Sleep(300)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 7870, 2800, 15500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0000)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_6492')
    def lambda_6492():
        ChrJumpTo(0x00FE, 5450, 0, 13130, 800, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_6492)

    @scena.Lambda('lambda_64B0')
    def lambda_64B0():
        OP_99(0x00FE, 0x0A, 0x0C, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_64B0)

    WaitForThreadExit(0x00FE, 0x0000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 0)
    Sleep(100)

    ChrJumpTo(0x00FE, 1150, 0, 10350, 500, 4000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0014 offset: 0x64F0
@scena.Code('func_14_64F0')
def func_14_64F0():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 12)
    ChrWalkTo(0x00FE, 4340, 0, -530, 10000, 0x00)
    ChrWalkTo(0x00F9, 12070, 0, 7110, 10000, 0x00)
    PlaySE(216, 0x00, 0x64)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 13)

    @scena.Lambda('lambda_6548')
    def lambda_6548():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_6548)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x0104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0002)
    Sleep(100)

    @scena.Lambda('lambda_65F3')
    def lambda_65F3():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_65F3)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x03, 0xFF, 0x0104, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 11)

    Return()

# id: 0x0015 offset: 0x669E
@scena.Code('func_15_669E')
def func_15_669E():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 4340, 0, -530, 10000, 0x00)
    ChrWalkTo(0x00FE, 11370, 0, 8440, 10000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_66F1')
    def lambda_66F1():
        ChrJumpTo(0x00FE, 13040, 0, 13000, 3500, 7000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_66F1)

    Sleep(300)

    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_671E')
    def lambda_671E():
        OP_99(0x00FE, 0x00, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_671E)

    Sleep(100)

    PlaySE(502, 0x00, 0x64)
    Sleep(100)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 3530, 13500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 0)
    WaitForThreadExit(0x00FE, 0x0000)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x00FE, 11610, 0, 6230, 200, 5000)
    ChrSetChipByIndex(0x00FE, 8)
    ChrSetSubChip(0x00FE, 0)
    PlaySE(164, 0x00, 0x64)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0016 offset: 0x67CC
@scena.Code('func_16_67CC')
def func_16_67CC():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 15)
    ChrWalkTo(0x00FE, 4340, 0, -530, 10000, 0x00)
    ChrWalkTo(0x00FE, 13310, 0, 13930, 10000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 16)

    @scena.Lambda('lambda_681F')
    def lambda_681F():
        OP_99(0x00FE, 0x00, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_681F)

    PlaySE(504, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_687F')
    def lambda_687F():
        OP_99(0x00FE, 0x01, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_687F)

    PlaySE(504, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 13310, 800, 15900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0002)
    Sleep(100)

    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_68E9')
    def lambda_68E9():
        OP_99(0x00FE, 0x01, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_68E9)

    @scena.Lambda('lambda_68F9')
    def lambda_68F9():
        ChrWalkTo(0x00FE, 13360, 500, 14600, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_68F9)

    PlaySE(504, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 13310, 800, 16500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0000)
    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 0)
    ChrJumpTo(0x00FE, 11610, 0, 6230, 200, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0017 offset: 0x6985
@scena.Code('func_17_6985')
def func_17_6985():
    Sleep(100)

    ChrClearFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 18)
    ChrWalkTo(0x00FE, 4340, 0, -530, 10000, 0x00)
    ChrWalkTo(0x00FE, 12600, 0, 9150, 10000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 30)

    @scena.Lambda('lambda_69D8')
    def lambda_69D8():
        OP_99(0x00FE, 0x00, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_69D8)

    ChrSetFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_69F7')
    def lambda_69F7():
        ChrJumpTo(0x00FE, 12930, 3530, 13000, 4000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_69F7)

    OP_99(0x00FE, 0x00, 0x03, 3500)
    ChrSetSubChip(0x00FE, 3)
    ChrSetChipByIndex(0x00FE, 30)
    WaitForThreadExit(0x00FE, 0x0000)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0106, 0x03, 0x00, func_18_6B86)
    Sleep(200)

    OP_7C(100, 0, 5000, 1000)
    OP_99(0x00FE, 0x04, 0x07, 1500)
    OP_99(0x00FE, 0x04, 0x07, 1500)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    @scena.Lambda('lambda_6AA5')
    def lambda_6AA5():
        OP_99(0x00FE, 0x08, 0x0F, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6AA5)

    Sleep(600)

    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(100, 0, 5000, 1000)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_6B1E')
    def lambda_6B1E():
        ChrJumpTo(0x00FE, 13510, 0, 11970, 500, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_6B1E)

    @scena.Lambda('lambda_6B3C')
    def lambda_6B3C():
        OP_99(0x00FE, 0x10, 0x17, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6B3C)

    WaitForThreadExit(0x00FE, 0x0000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetSubChip(0x00FE, 0)
    Sleep(100)

    ChrJumpTo(0x00FE, 12690, 0, 5850, 500, 5000)

    Return()

# id: 0x0018 offset: 0x6B86
@scena.Code('func_18_6B86')
def func_18_6B86():
    Sleep(200)

    def _loc_6B8B(): pass

    label('loc_6B8B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6BE3',
    )

    PlaySE(801, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 12930, 4000, 14500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6BDB',
    )

    OP_23(0x0321)

    Jump('loc_6BE3')

    def _loc_6BDB(): pass

    label('loc_6BDB')

    Sleep(100)

    Jump('loc_6B8B')

    def _loc_6BE3(): pass

    label('loc_6BE3')

    Return()

# id: 0x0019 offset: 0x6BE4
@scena.Code('func_19_6BE4')
def func_19_6BE4():
    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    Sleep(1000)

    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    Sleep(1000)

    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    Sleep(1000)

    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)

    Return()

# id: 0x001A offset: 0x6C86
@scena.Code('func_1A_6C86')
def func_1A_6C86():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_6D03'),
        (0x00000001, 'loc_6D09'),
        (-1, 'loc_6D0F'),
    )

    def _loc_6D03(): pass

    label('loc_6D03')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_6D0F')

    def _loc_6D09(): pass

    label('loc_6D09')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_6D0F')

    def _loc_6D0F(): pass

    label('loc_6D0F')

    Return()

# id: 0x001B offset: 0x6D10
@scena.Code('func_1B_6D10')
def func_1B_6D10():
    MapClearFlags(0x00000001)
    CameraMove(97010, 0, 95840, 0)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
