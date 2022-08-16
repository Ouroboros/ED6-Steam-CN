import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1201   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1201.x'
    header.mapIndex       = 61
    header.bgm            = 29
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
        ('ED6_DT09/CH10290._CH', 'ED6_DT09/CH10290P._CP'),
        ('ED6_DT09/CH10291._CH', 'ED6_DT09/CH10291P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '古罗尼山道方向',
            x                   = -348670,
            z                   = 150,
            y                   = 8790,
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
        ScenaNpcData(
            name                = '拉文努山道方向',
            x                   = -251150,
            z                   = 0,
            y                   = 36410,
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
        ScenaNpcData(
            name                = '柏斯方向',
            x                   = -206940,
            z                   = 0,
            y                   = -15170,
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

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -245780,
            z           = 10,
            y           = -13290,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -283410,
            z           = 510,
            y           = 3500,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -257890,
            z           = -80,
            y           = -19810,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -297320,
            z           = -10,
            y           = -50,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -321660,
            z           = 0,
            y           = 7860,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1E6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -258500,
            y           = -2000,
            z           = 23000,
            range       = -243800,
            dword_10    = 0x000007D0,
            dword_14    = 0x00005EEC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -268700,
            y           = -360,
            z           = -4580,
            range       = -270570,
            dword_10    = 0x0000041A,
            dword_14    = 0xFFFFD79C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x226
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -234940,
            triggerZ            = 1020,
            triggerY            = -22700,
            triggerRange        = 1000,
            actorX              = -234380,
            actorZ              = 1020,
            actorY              = -22890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -254930,
            triggerZ            = 0,
            triggerY            = 140,
            triggerRange        = 1500,
            actorX              = -254930,
            actorZ              = 1300,
            actorY              = 140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -261790,
            triggerZ            = 0,
            triggerY            = -2900,
            triggerRange        = 1500,
            actorX              = -261790,
            actorZ              = 1500,
            actorY              = -2900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -267850,
            triggerZ            = 10,
            triggerY            = -14960,
            triggerRange        = 1000,
            actorX              = -270790,
            actorZ              = -1000,
            actorY              = -16940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2C9',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_30D)

    def _loc_2C9(): pass

    label('loc_2C9')

    Return()

# id: 0x0001 offset: 0x2CA
@scena.Code('func_01_2CA')
def func_01_2CA():
    OP_16(0x02, 4000, -400000, -127000, 2293786)

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F3',
    )

    OP_1B(0x02, 0x00, 0x0005)

    def _loc_2F3(): pass

    label('loc_2F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0360, 5, 0x1B05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_305',
    )

    OP_6F(0x0000, 0)

    Jump('loc_30C')

    def _loc_305(): pass

    label('loc_305')

    OP_6F(0x0000, 60)

    def _loc_30C(): pass

    label('loc_30C')

    Return()

# id: 0x0002 offset: 0x30D
@scena.Code('func_02_30D')
def func_02_30D():
    EventBegin(0x00)
    CameraMove(-249620, -10, 18100, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -249620, -10, 18100, 180)
    ChrSetPos(0x0106, -249620, -10, 18100, 180)
    ChrSetPos(0x00F8, -249620, -10, 18100, 180)
    ChrSetPos(0x00F9, -249620, -10, 18100, 180)
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x396
@scena.Code('func_03_396')
def func_03_396():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 1, 0x1A11)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_488',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40E',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    ChrTalk(
        0x0106,
        (
            '#0050300792V#552F这边是拉文努村',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300793V等手边的工作\n',
            '告一段落后再过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46D')

    def _loc_40E(): pass

    label('loc_40E')

    ChrTalk(
        0x0106,
        (
            '#0050300794V#555F喂……\n',
            '这边是拉文努村啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300795V等手边的工作\n',
            '告一段落后再过去啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46D(): pass

    label('loc_46D')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_488(): pass

    label('loc_488')

    Return()

# id: 0x0004 offset: 0x489
@scena.Code('func_04_489')
def func_04_489():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A1',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_505',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490088V#1002F啊，好像走过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490089V#1002F拉文努村是在\n',
            '这座桥之前往北走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_686')

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_589',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_529',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_530')

    def _loc_529(): pass

    label('loc_529')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_530(): pass

    label('loc_530')

    ChrTalk(
        0x0103,
        (
            '#0030490090V#022F稍微走过头了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490091V拉文努村是在\n',
            '这座桥之前往北走哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_686')

    def _loc_589(): pass

    label('loc_589')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_608',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A6',
    )

    Jump('loc_5AD')

    def _loc_5A6(): pass

    label('loc_5A6')

    ChrTurnDirection(0x0104, 0x0000, 400)

    def _loc_5AD(): pass

    label('loc_5AD')

    ChrTalk(
        0x0104,
        (
            '#0040490092V#030F看来好像走过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490093V拉文努村是在\n',
            '这座桥之前往北走哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_686')

    def _loc_608(): pass

    label('loc_608')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_686',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_625',
    )

    Jump('loc_62C')

    def _loc_625(): pass

    label('loc_625')

    ChrTurnDirection(0x0108, 0x0000, 400)

    def _loc_62C(): pass

    label('loc_62C')

    ChrTalk(
        0x0108,
        (
            '#0080490094V#070F看来好像走过头了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490095V拉文努村是在\n',
            '这座桥之前往北走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_686(): pass

    label('loc_686')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6A1(): pass

    label('loc_6A1')

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9C3',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7EF',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_713',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490096V#050F要去拉文努村的话该往北才对。\n',
            '没有时间绕远路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EC')

    def _loc_713(): pass

    label('loc_713')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_760',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490097V#025F拉文努村在北边呢……\n',
            '没有时间绕远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EC')

    def _loc_760(): pass

    label('loc_760')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490098V#072F拉文努村在北边吧。\n',
            '没有时间绕远路啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EC')

    def _loc_7AB(): pass

    label('loc_7AB')

    ChrTalk(
        0x0101,
        (
            '#0010490099V#1015F拉文努村在北边吧。\n',
            '现在不是绕远路的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7EC(): pass

    label('loc_7EC')

    Jump('loc_9A8')

    def _loc_7EF(): pass

    label('loc_7EF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_865',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490100V#053F要去拉文努村的话该往北吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490101V#050F带着同行者，\n',
            '可没有时间绕远路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A5')

    def _loc_865(): pass

    label('loc_865')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490102V#025F啊，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490103V带着同行者，\n',
            '可没有时间绕远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A5')

    def _loc_8D0(): pass

    label('loc_8D0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_940',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490104V#073F哦，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490105V#070F带着同行者，\n',
            '可没有时间绕远路啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A5')

    def _loc_940(): pass

    label('loc_940')

    ChrTalk(
        0x0101,
        (
            '#0010490106V#1015F啊，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490107V毕竟队伍中有同行者，\n',
            '绕远路的事之后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A5(): pass

    label('loc_9A5')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_9A8(): pass

    label('loc_9A8')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_9C3(): pass

    label('loc_9C3')

    Return()

# id: 0x0005 offset: 0x9C4
@scena.Code('func_05_9C4')
def func_05_9C4():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AF2',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A1A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490108V#050F拉文努村在北边吧。\n',
            '没有时间绕远路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF')

    def _loc_A1A(): pass

    label('loc_A1A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A65',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490109V#020F拉文努村在北边吧。\n',
            '没有时间绕远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF')

    def _loc_A65(): pass

    label('loc_A65')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AAE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490110V#070F拉文努村在北边。\n',
            '没有时间绕远路啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF')

    def _loc_AAE(): pass

    label('loc_AAE')

    ChrTalk(
        0x0101,
        (
            '#0010490111V#1000F拉文努村在北边吧。\n',
            '现在不是绕远路的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEF(): pass

    label('loc_AEF')

    Jump('loc_CA3')

    def _loc_AF2(): pass

    label('loc_AF2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B65',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490112V#050F要去拉文努村的话该往北才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490113V带着同行者，\n',
            '可没有时间绕远路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA0')

    def _loc_B65(): pass

    label('loc_B65')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490114V#020F啊，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490103V带着同行者，\n',
            '可没有时间绕远路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA0')

    def _loc_BD0(): pass

    label('loc_BD0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C3B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490116V#070F哦，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490117V带着同行者，\n',
            '可没有时间绕远路啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA0')

    def _loc_C3B(): pass

    label('loc_C3B')

    ChrTalk(
        0x0101,
        (
            '#0010490118V#1000F啊，拉文努村在北边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490107V毕竟队伍中有同行者，\n',
            '绕远路的事之后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA0(): pass

    label('loc_CA0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_CA3(): pass

    label('loc_CA3')

    OP_59()
    Fade(1000)
    ChrSetPos(0x0101, -332600, 40, 8970, 90)
    ChrSetPos(0x00F7, -332600, 40, 8970, 90)
    ChrSetPos(0x00F8, -332600, 40, 8970, 90)
    ChrSetPos(0x00F9, -332600, 40, 8970, 90)
    ChrSetPos(0x0147, -332600, 40, 8970, 90)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0006 offset: 0xD07
@scena.Code('func_06_D07')
def func_06_D07():
    UnlockAchievement(0x02, 0x01CC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0360, 5, 0x1B05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_D7B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0360, 5, 0x1B05))

    Jump('loc_DE1')

    def _loc_D7B(): pass

    label('loc_D7B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_DE1(): pass

    label('loc_DE1')

    Jump('loc_E15')

    def _loc_DE4(): pass

    label('loc_DE4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_E15(): pass

    label('loc_E15')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xE23
@scena.Code('func_07_E23')
def func_07_E23():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　拉文努村　　１４７塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xE72
@scena.Code('func_08_E72')
def func_08_E72():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　柏斯市　　　１４０塞尔矩\n',
            '西　古罗尼山顶　３０１塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xEDE
@scena.Code('func_09_EDE')
def func_09_EDE():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F16')
    def lambda_0F16():
        CameraMove(-270600, 50, -15450, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0F16)

    @scena.Lambda('lambda_0F2E')
    def lambda_0F2E():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0F2E)

    @scena.Lambda('lambda_0F3E')
    def lambda_0F3E():
        OP_6C(0, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0F3E)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FC5',
    )

    OP_C0(0x0E, 0x0000000B, 0xFFFBE9B6, 0x0000000A, 0xFFFFC590, 0x000000E1, 0xFFFBDE3A, 0xFFFFFC18, 0xFFFFBDD4)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_FD4')

    def _loc_FC5(): pass

    label('loc_FC5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FD4',
    )

    EventEnd(0x01)

    def _loc_FD4(): pass

    label('loc_FD4')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
