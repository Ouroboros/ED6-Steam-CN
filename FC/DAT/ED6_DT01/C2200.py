import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2200.x'
    header.mapIndex       = 84
    header.bgm            = 31
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
            word_3A         = 84,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
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

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20085._CH', 'ED6_DT06/CH20085P._CP'),
    ]

# id: 0x10001 offset: 0x126
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '基库',
            x                   = 800,
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
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
            name                = '黑衣男子',
            x                   = -11460,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
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
            name                = '黑衣男子',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 90,
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
            name                = '弗科特老人',
            x                   = 620,
            z                   = 550,
            y                   = -2470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚间道方向',
            x                   = 1330,
            z                   = -430,
            y                   = -46450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1E6
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1E6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1E6
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1FE',
    )

    OP_72(0x0002, 0x0008)

    Jump('loc_1FE')

    def _loc_1FE(): pass

    label('loc_1FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_20C',
    )

    Event(0, func_05_946)

    Jump('loc_214')

    def _loc_20C(): pass

    label('loc_20C')

    MapClearFlags(0x40000000)
    FormationAddMember(0xFF, 0xFF)

    def _loc_214(): pass

    label('loc_214')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_220'),
        (-1, 'loc_236'),
    )

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_233',
    )

    SetScenaFlags(ScenaFlag(0x0087, 0, 0x438))
    Event(0, func_03_29D)

    def _loc_233(): pass

    label('loc_233')

    Jump('loc_236')

    def _loc_236(): pass

    label('loc_236')

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x248
@scena.Code('func_01_248')
def func_01_248():
    OP_16(0x02, 4000, -128000, -140000, 196688)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_266',
    )

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_273',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    Jump('loc_278')

    def _loc_273(): pass

    label('loc_273')

    OP_71(0x000A, 0x0004)

    def _loc_278(): pass

    label('loc_278')

    OP_B0(0x0000, 0x78)
    OP_1C(0x00, 0x00, 0x0008)
    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x287
@scena.Code('func_02_287')
def func_02_287():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_29C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_287')

    def _loc_29C(): pass

    label('loc_29C')

    Return()

# id: 0x0003 offset: 0x29D
@scena.Code('func_03_29D')
def func_03_29D():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(3700, 2600, -22200, 0)
    CameraSetDistance(4000, 0)
    OP_6C(333000, 0)
    ChrSetPos(0x0008, 2780, 2600, -22200, 0)
    ChrSetPos(0x0101, 3920, -540, -27770, 0)
    ChrSetPos(0x0102, 2820, -530, -28580, 0)
    ChrSetPos(0x0105, 3690, -460, -29430, 0)
    ChrSetPos(0x0106, 4740, -440, -28690, 0)
    OP_12(0x00007D00, 0x00027100, 0x00000000)

    @scena.Lambda('lambda_032F')
    def lambda_032F():
        CameraMove(0, 8800, 6500, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_032F)

    @scena.Lambda('lambda_0347')
    def lambda_0347():
        OP_6C(57000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0347)

    @scena.Lambda('lambda_0357')
    def lambda_0357():
        OP_67(0, 11290, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0357)

    @scena.Lambda('lambda_036F')
    def lambda_036F():
        CameraSetDistance(10000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_036F)

    FadeIn(2000, 0)
    OP_12(0x00007D00, 0x00057E40, 0x00001388)
    ChrClearFlags(0x0008, 0x0080)
    ChrWalkTo(0x0008, 9530, 12000, 4120, 14000, 0x00)
    CreateThread(0x0008, 0x01, 0x00, func_04_92D)
    OP_97(0x0008, 0, 6500, -600000, 14000, 0x0001)
    TerminateThread(0x0008, 0xFF)
    Fade(1000)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(3940, -520, -28440, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010061146V#002F那座建筑物是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061147V#057F巴伦诺灯塔……\n',
            '是卢安市辖下的设施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061148V我记得这里只住着\n',
            '一个看守灯塔的老头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061149V#042F但是，不会有错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061150V我想那些袭击老师的犯人\n',
            '就在这座建筑物里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061151V#012F那就是说，\n',
            '犯人很有可能占领了灯塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061152V#002F看起来……\n',
            '好像只有那一个入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061153V总之只能进去看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061154V#042F好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0105, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061155V#052F#2P等一下。\n',
            '小姑娘，难道你也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061156V#049F我想亲眼看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061157V#055F#2P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0106, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061158V#043F犯人到底是什么人，\n',
            '为什么要对老师和孩子们下这种毒手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061159V#043F所以……请让我也一起去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061160V#055F#2P就、就算你这样说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06F8')
    def lambda_06F8():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06F8)

    @scena.Lambda('lambda_0706')
    def lambda_0706():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0706)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010061161V#006F#1P啊～真是的。\n',
            '别那么小气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061162V#006F我们能找到犯人，\n',
            '可全是科洛丝的功劳哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061163V#010F#3P她的身手我们可以担保。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061164V我想至少不用担心\n',
            '她会成为我们的负担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061165V#048F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061166V#053F#2P嘁……随你们便吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061167V#057F但是你们要知道，\n',
            '对方可是打倒了卡露娜的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061168V万事小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0106, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061169V#040F是，我一定会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061170V#006F#1P那就这么定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061171V#012F#3P嗯……\n',
            '我们快进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003E, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x92D
@scena.Code('func_04_92D')
def func_04_92D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_945',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x3C),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_04_92D')

    def _loc_945(): pass

    label('loc_945')

    Return()

# id: 0x0005 offset: 0x946
@scena.Code('func_05_946')
def func_05_946():
    OP_72(0x000A, 0x0004)
    EventBegin(0x00)
    CameraMove(130, 21350, 6270, 0)
    OP_6C(270000, 0)
    CameraSetDistance(3770, 0)
    OP_72(0x0002, 0x0008)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetChipByIndex(0x000A, 4)
    ChrSetChipByIndex(0x0106, 5)
    ChrSetPos(0x0009, 5080, 25000, 6100, 0)
    ChrSetPos(0x000A, 5080, 25000, 6100, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetPos(0x0101, 5080, 25000, 6100, 0)
    ChrSetPos(0x0102, 5080, 25000, 6100, 0)
    ChrSetPos(0x0105, 5080, 25000, 6100, 0)
    ChrSetPos(0x0106, 5080, 25000, 6100, 0)
    OP_6F(0x0001, 40)
    OP_70(0x0001, 80)

    @scena.Lambda('lambda_0A12')
    def lambda_0A12():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A12)

    @scena.Lambda('lambda_0A22')
    def lambda_0A22():
        CameraMove(-2320, 25000, -1320, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0A22)

    ChrSetPos(0x0009, 5080, 25000, 6100, 0)
    ChrSetPos(0x000A, 5080, 25000, 6100, 0)
    CreateThread(0x0009, 0x01, 0x00, func_06_10E4)
    Sleep(1000)

    CreateThread(0x000A, 0x01, 0x00, func_06_10E4)
    Sleep(2500)

    CreateThread(0x0106, 0x01, 0x00, func_07_11D5)
    Sleep(300)

    CreateThread(0x0101, 0x01, 0x00, func_06_10E4)
    Sleep(300)

    CreateThread(0x0102, 0x01, 0x00, func_06_10E4)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, func_06_10E4)
    Sleep(1750)

    OP_4A(0x0106, 1)

    ExecExpressionWithValue(
        0x0106,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0106, 5)
    ChrSetSubChip(0x0106, 0)
    Sleep(50)

    TerminateThread(0x0101, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(50)

    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    Sleep(50)

    TerminateThread(0x0105, 0xFF)

    ExecExpressionWithValue(
        0x0105,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0105, 0)
    Fade(1000)
    CameraMove(-240, 25000, -1010, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020061314V#014F逃跑用的钢索！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061315V#005F还、还真是\n',
            '准备得很周到啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061316V#057F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061317V……混蛋秘书和那帮蠢货\n',
            '就交给你们处理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061318V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 800)

    ChrTalk(
        0x0106,
        (
            '#0050061319V#054F我要去追那些家伙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061320V你们几个，把这次事件报告给嘉恩，\n',
            '然后听他的指示吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 270, 800)
    OP_4B(0x0106, 1)

    ChrTalk(
        0x0105,
        (
            '#0060061321V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        10,
        0,
        (
            TXT(0x00, '『好吧，我也去！』\n'),
            TXT(0x01, '『真、真是乱来的家伙……』\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D4B'),
        (0x00000001, 'loc_E18'),
        (-1, 'loc_EE1'),
    )

    def _loc_D4B(): pass

    label('loc_D4B')

    ChrTalk(
        0x0101,
        (
            '#0010061322V#005F好吧，我也去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D76')
    def lambda_0D76():
        ChrWalkTo(0x00FE, -2200, 25000, -1100, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D76)

    Sleep(260)

    TerminateThread(0x0101, 0xFF)
    ChrSetSubChip(0x0101, 6)

    ChrTalk(
        0x0102,
        (
            '#0020061323V#012F等一下，艾丝蒂尔。\n',
            '阿加特不是说了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061324V#012F不能把市长秘书和\n',
            '『渡鸦帮』的成员们丢下不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE1')

    def _loc_E18(): pass

    label('loc_E18')

    ChrTalk(
        0x0101,
        (
            '#0010061325V#004F真、真是乱来的家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061326V#004F约修亚，我们也要追吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061327V#012F不……\n',
            '阿加特不是说了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061328V#012F不能把市长秘书和\n',
            '『渡鸦帮』的成员们丢下不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE1')

    def _loc_EE1(): pass

    label('loc_EE1')

    ChrTalk(
        0x0105,
        (
            '#0060061329V#043F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061330V虽说是自作自受，\n',
            '但是他腿上受了伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061331V#002F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061332V#007F虽然很不甘心，\n',
            '不过也只能把追捕的任务交给阿加特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    OP_24(0x01C5, 0x5F)
    Sleep(200)

    OP_24(0x01C5, 0x5A)
    Sleep(200)

    OP_24(0x01C5, 0x55)
    Sleep(200)

    OP_24(0x01C5, 0x50)
    Sleep(200)

    OP_24(0x01C5, 0x4B)
    Sleep(200)

    OP_24(0x01C5, 0x46)
    Sleep(200)

    OP_24(0x01C5, 0x41)
    Sleep(200)

    OP_23(0x01C5)
    OP_0D()
    OP_21()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '……就这样，艾丝蒂尔他们\n',
            '成功取回了特蕾莎院长被抢走的捐款。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '然后，他们把市长秘书和那些不良青年\n',
            '关押在玛诺利亚的风车小屋里，\n',
            '这时，天已经开始亮了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapClearFlags(0x40000000)
    OP_28(0x003E, 0x01, 0x0080)
    OP_28(0x003E, 0x01, 0x0100)
    Sleep(1000)

    MapSetFlags(0x00100000)
    PlaySE(13, 0x00, 0x64)
    Sleep(2500)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2300._SN', 0, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x10E4
@scena.Code('func_06_10E4')
def func_06_10E4():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 7280, 25000, 5810, 6000, 0x00)
    ChrWalkTo(0x00FE, 7110, 25000, 2430, 6000, 0x00)
    ChrWalkTo(0x00FE, 3800, 25000, -1100, 6000, 0x00)
    ChrWalkTo(0x00FE, -1900, 25000, -1100, 6000, 0x00)
    ChrJumpTo(0x00FE, -2940, 26000, -1820, 1000, 6000)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveTo(0x00FE, -3610, 25000, -2100, 4000, 0x00)
    ChrMoveTo(0x00FE, -3610, 24000, -2100, 6000, 0x00)
    ChrMoveTo(0x00FE, -3610, 23000, -2100, 8000, 0x00)
    ChrMoveTo(0x00FE, -3610, 21000, -2100, 10000, 0x00)
    ChrMoveTo(0x00FE, -3610, 5000, -2100, 13000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0007 offset: 0x11D5
@scena.Code('func_07_11D5')
def func_07_11D5():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 7280, 25000, 5810, 6000, 0x00)
    ChrWalkTo(0x00FE, 7110, 25000, 2430, 6000, 0x00)
    ChrWalkTo(0x00FE, 3800, 25000, -1100, 6000, 0x00)
    ChrWalkTo(0x00FE, -1900, 25000, -1100, 6000, 0x00)
    ChrJumpTo(0x00FE, -2940, 26000, -1820, 1000, 6000)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveTo(0x00FE, -3610, 25000, -2100, 4000, 0x00)
    ChrMoveTo(0x00FE, -3610, 24000, -2100, 6000, 0x00)
    ChrMoveTo(0x00FE, -3610, 23000, -2100, 8000, 0x00)
    ChrMoveTo(0x00FE, -3610, 21000, -2100, 10000, 0x00)
    ChrMoveTo(0x00FE, -3610, 5000, -2100, 13000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0008 offset: 0x12C1
@scena.Code('func_08_12C1')
def func_08_12C1():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
