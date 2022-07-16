import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4280_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4280   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾莉茜雅女王'),
    TXT(0x02, '尤莉亚中尉'),
    TXT(0x03, '约修亚'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '金'),
    TXT(0x06, '特务兵'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4280.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB4B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 11510,
            z                   = 0,
            y                   = -154850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 11510,
            y           = -1000,
            z           = -154850,
            range       = 4000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = -102220,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = -102220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_204',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_212',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0004)

    def _loc_212(): pass

    label('loc_212')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23C',
    )

    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 1)
    SetChrChipByIndex(0x0138, 2)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_23C(): pass

    label('loc_23C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Return,
        ),
        'loc_248',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_248(): pass

    label('loc_248')

    Return()

# id: 0x0001 offset: 0x249
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26B',
    )

    OP_1B(0x01, 0x00, 0x0006)
    OP_1B(0x03, 0x00, 0x0007)
    OP_6F(0x0000, 120)

    def _loc_26B(): pass

    label('loc_26B')

    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            Expr.Return,
        ),
        'loc_285',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0001, 0x0010)
    OP_1C(0x01, 0x00, 0x0009)

    def _loc_285(): pass

    label('loc_285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_295',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_295(): pass

    label('loc_295')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x29F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2B4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('ReInit')

    def _loc_2B4(): pass

    label('loc_2B4')

    Return()

# id: 0x0003 offset: 0x2B5
@scena.Code('func_03_2B5')
def func_03_2B5():
    EventBegin(0x00)
    CameraMove(9400, 0, -139720, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0104, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    SetChrPos(0x0102, 12770, 0, -140130, 135)
    SetChrPos(0x0104, 12770, 0, -140130, 135)
    SetChrPos(0x0108, 12770, 0, -140130, 135)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    OP_73(0x0000)
    OP_6F(0x0000, 60)
    OP_72(0x0000, 0x0010)

    @scena.Lambda('lambda_037D')
    def lambda_037D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_037D)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        ChrWalkTo(0x00FE, 10050, 0, -139340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_038F)

    Sleep(500)

    @scena.Lambda('lambda_03AF')
    def lambda_03AF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_03AF)

    @scena.Lambda('lambda_03C1')
    def lambda_03C1():
        ChrWalkTo(0x00FE, 9570, 0, -140380, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_03C1)

    Sleep(500)

    @scena.Lambda('lambda_03E1')
    def lambda_03E1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_03E1)

    @scena.Lambda('lambda_03F3')
    def lambda_03F3():
        ChrWalkTo(0x00FE, 11260, 0, -140020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_03F3)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 180, 400)
    WaitForThreadExit(0x0104, 0x0001)
    SetChrDirection(0x0104, 90, 400)

    ChrTalk(
        0x0102,
        (
            '#010F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0108, 400)

    ChrTalk(
        0x0104,
        (
            '#030F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x4A1
@scena.Code('func_04_4A1')
def func_04_4A1():
    EventBegin(0x00)
    CameraMove(540, 0, -102880, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000A, 0, 0, -103520, 0)
    SetChrPos(0x0101, -1430, 0, -104260, 37)
    SetChrPos(0x0008, 1550, 0, -103430, 281)
    SetChrPos(0x0009, 1310, 0, -104570, 330)
    SetChrPos(0x0105, 2540, 0, -103830, 273)
    SetChrPos(0x000B, -460, 0, -105370, 12)
    SetChrPos(0x000C, 710, 0, -106060, 348)
    SetChrPos(0x0103, -2300, 0, -103380, 90)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#010F果然没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131454V就在最近一段时间，\n',
            '这里有过频繁出入的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F也许是使用了备用钥匙，\n',
            '然后进去做了些什么吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看来是有必要进去调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 180, 0, -102540, 2000, 0x00)
    SetChrDirection(0x0008, 0, 400)
    Sleep(500)

    FadeOut(2000, 0, -1)
    OP_70(0x0001, 60)
    OP_73(0x0001)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4241._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x66A
@scena.Code('func_05_66A')
def func_05_66A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7BE',
    )

    EventBegin(0x01)
    OP_4A(0x000D, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_726',
    )

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120525V哦，希尔丹夫人。\n',
            '您来这种地方有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120526V您也是知道的，\n',
            '这里禁止无关人员进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120527V如果没事的话，\n',
            '请快点离开这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_778')

    def _loc_726(): pass

    label('loc_726')

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120528V这里禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120529V可疑人员一律逮捕。\n',
            '请给我注意好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_778(): pass

    label('loc_778')

    Fade(1000)
    SetChrPos(0x0000, 9440, 0, -153980, 270)
    SetChrPos(0x0001, 9440, 0, -153980, 270)
    SetChrPos(0x0002, 9440, 0, -153980, 270)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x01)
    OP_4B(0x000D, 255)

    def _loc_7BE(): pass

    label('loc_7BE')

    Return()

# id: 0x0006 offset: 0x7BF
@scena.Code('func_06_7BF')
def func_06_7BF():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_826',
    )

    ChrTalk(
        0x0102,
        (
            '#0020131123V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131124V赶快从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_92F')

    def _loc_826(): pass

    label('loc_826')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B7',
    )

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131127V#035F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_92F')

    def _loc_8B7(): pass

    label('loc_8B7')

    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131130V#072F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_92F(): pass

    label('loc_92F')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0x94B
@scena.Code('func_07_94B')
def func_07_94B():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9B2',
    )

    ChrTalk(
        0x0102,
        (
            '#0020131123V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131124V赶快从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABB')

    def _loc_9B2(): pass

    label('loc_9B2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A43',
    )

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131127V#035F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABB')

    def _loc_A43(): pass

    label('loc_A43')

    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131130V#072F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABB(): pass

    label('loc_ABB')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0008 offset: 0xAD7
@scena.Code('func_08_AD7')
def func_08_AD7():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xB2B
@scena.Code('func_09_B2B')
def func_09_B2B():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
