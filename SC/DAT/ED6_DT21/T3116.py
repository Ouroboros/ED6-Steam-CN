import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3116_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3116   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3116.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0001
    header.entryFunction  = 0x000C
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3116_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00137._CH', 'ED6_DT07/CH00137P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = -2000,
            z                   = 0,
            y                   = 3410,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = -120,
            z                   = 0,
            y                   = 13020,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = -1920,
            z                   = 0,
            y                   = 14190,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x132
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x132
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -340,
            triggerZ            = 0,
            triggerY            = 15310,
            triggerRange        = 1000,
            actorX              = -340,
            actorZ              = 500,
            actorY              = 15310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4350,
            triggerZ            = 0,
            triggerY            = 2150,
            triggerRange        = 1000,
            actorX              = 4350,
            actorZ              = 500,
            actorY              = 2150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4600,
            triggerZ            = 0,
            triggerY            = 15420,
            triggerRange        = 1000,
            actorX              = 4600,
            actorZ              = 500,
            actorY              = 15420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A8',
    )

    Jump('loc_1CE')

    def _loc_1A8(): pass

    label('loc_1A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BE',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_1BE(): pass

    label('loc_1BE')

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE',
    )

    ChrSetFlags(0x0008, 0x0010)

    def _loc_1CE(): pass

    label('loc_1CE')

    Return()

# id: 0x0001 offset: 0x1CF
@scena.Code('func_01_1CF')
def func_01_1CF():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EE',
    )

    OP_79(0xFF, 0x0002)
    OP_7A(0x08, 0x0002)
    OP_7B()
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)

    def _loc_1EE(): pass

    label('loc_1EE')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)

    Return()

# id: 0x0002 offset: 0x1FB
@scena.Code('func_02_1FB')
def func_02_1FB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_708',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 7, 0x20CF)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B8',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……？\n',
            '哦，是游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久不见。\n',
            '你们看起来很精神，这就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过中央工房\n',
            '整体都很忙碌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '因为从照明到实验材料，\n',
            '全都不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '那个用枪的人怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F你说奥利维尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F那家伙已经\n',
            '回国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……回国了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道\n',
            '奥利维尔先生是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，他是外国友人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还想让他看看\n',
            '完成了的新型枪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过……\n',
            '现在也不是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这种现象持续下去的话，\n',
            '我的研究成果就要被推翻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1020F加、加鲁诺先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1048F（看上去一副走投无路的样子……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0419, 7, 0x20CF))

    Jump('loc_705')

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_5B1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_533',
    )

    ChrTalk(
        0x00FE,
        (
            '如果这种现象持续下去的话\n',
            '我的研究成果就要被推翻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AE')

    def _loc_533(): pass

    label('loc_533')

    ChrTalk(
        0x00FE,
        (
            '枪不能使用了\n',
            '确实很打击人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过也不能一直\n',
            '这么消沉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为一两次挫折就倒下去的话\n',
            '还谈什么伟大的发明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE(): pass

    label('loc_5AE')

    Jump('loc_705')

    def _loc_5B1(): pass

    label('loc_5B1')

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_625',
    )

    ChrTalk(
        0x00FE,
        (
            '如果这种现象持续下去的话\n',
            '我的研究成果就要被推翻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_625(): pass

    label('loc_625')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A3',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易快要使\n',
            '新型枪商品化了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟、竟然在这个节骨眼儿上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，好像因为打击\n',
            '而笑个不停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_705')

    def _loc_6A3(): pass

    label('loc_6A3')

    ChrTalk(
        0x00FE,
        (
            '好不容易快要使\n',
            '新型枪商品化了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟、竟然在这个节骨眼儿上……\n',
            '因为受打击而停止研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_705(): pass

    label('loc_705')

    Jump('loc_D70')

    def _loc_708(): pass

    label('loc_708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_716',
    )

    Call(1, 0x0009)

    Jump('loc_D70')

    def _loc_716(): pass

    label('loc_716')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_724',
    )

    Call(1, 0x000B)

    Jump('loc_D70')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_732',
    )

    Call(1, 0x000A)

    Jump('loc_D70')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_78B',
    )

    ChrTalk(
        0x00FE,
        (
            '不装备『零式导力枪α』\n',
            '的话战斗结果是不计算的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要注意这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D70')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_799',
    )

    Call(1, 0x0008)

    Jump('loc_D70')

    def _loc_799(): pass

    label('loc_799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_7A7',
    )

    Call(1, 0x0001)

    Jump('loc_D70')

    def _loc_7A7(): pass

    label('loc_7A7')

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7C0',
    )

    Call(1, 0x0004)

    Jump('loc_D70')

    def _loc_7C0(): pass

    label('loc_7C0')

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7EB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_7E4',
    )

    Call(1, 0x0002)

    Jump('loc_7E8')

    def _loc_7E4(): pass

    label('loc_7E4')

    Call(1, 0x0000)

    def _loc_7E8(): pass

    label('loc_7E8')

    Jump('loc_D70')

    def _loc_7EB(): pass

    label('loc_7EB')

    If(
        (
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_B14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_8BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_856',
    )

    ChrTalk(
        0x00FE,
        (
            '地震的安全宣言也出来了，\n',
            '暂时能专注于研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请期待我的\n',
            '新型导力枪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BB')

    def _loc_856(): pass

    label('loc_856')

    ChrTalk(
        0x00FE,
        (
            '啊，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震的安全宣言也出来了，\n',
            '暂时能专注于研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请期待我的\n',
            '新型导力枪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_8BB(): pass

    label('loc_8BB')

    Jump('loc_B11')

    def _loc_8BE(): pass

    label('loc_8BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_990',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_917',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士好像\n',
            '在进行某种实验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有空的话我要\n',
            '不要去看一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98D')

    def _loc_917(): pass

    label('loc_917')

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士好像\n',
            '在进行某种实验，\n',
            '你知道具体内容吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我整理好文件\n',
            '要不要也去看看呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_98D(): pass

    label('loc_98D')

    Jump('loc_B11')

    def _loc_990(): pass

    label('loc_990')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_A41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9E4',
    )

    ChrTalk(
        0x00FE,
        (
            '你们看上去很忙，\n',
            '还在进行什么工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士真不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3E')

    def _loc_9E4(): pass

    label('loc_9E4')

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看上去很忙，\n',
            '还在进行什么工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士真不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A3E(): pass

    label('loc_A3E')

    Jump('loc_B11')

    def _loc_A41(): pass

    label('loc_A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_B11',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AA6',
    )

    ChrTalk(
        0x00FE,
        (
            '今天非常感谢。\n',
            '你们可帮了我大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后再有什么事的话\n',
            '你们也要帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B11')

    def _loc_AA6(): pass

    label('loc_AA6')

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天非常感谢。\n',
            '你们可帮了我大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后再有什么事的话\n',
            '你们也要帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B11(): pass

    label('loc_B11')

    Jump('loc_D70')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_BDC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B64',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然没有人来应聘……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是应聘资格\n',
            '定得太严格了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD9')

    def _loc_B64(): pass

    label('loc_B64')

    ChrTalk(
        0x00FE,
        (
            '呼，不过真让人感到为难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经等了很久了，\n',
            '竟然没有人来应聘……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是应聘资格\n',
            '定得太严格了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_BD9(): pass

    label('loc_BD9')

    Jump('loc_D70')

    def _loc_BDC(): pass

    label('loc_BDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_CA6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C3E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，终于准备完成了吗？\n',
            '接下来就是等待应聘的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个，没忘记什么吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA3')

    def _loc_C3E(): pass

    label('loc_C3E')

    ChrTalk(
        0x00FE,
        (
            '嗯，导力枪的调整ＯＫ了。\n',
            '书面手续也弄完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，准备完成。\n',
            '接下来就是等待应聘的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_CA3(): pass

    label('loc_CA3')

    Jump('loc_D70')

    def _loc_CA6(): pass

    label('loc_CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_D70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D19',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，导力枪的调整ＯＫ了。\n',
            '书面手续也弄完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，准备完成。\n',
            '接下来就是等待应聘的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D70')

    def _loc_D19(): pass

    label('loc_D19')

    ChrTalk(
        0x00FE,
        (
            '呼，真麻烦。\n',
            '偏偏这种时候来地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都准备好接下来要\n',
            '进行重要的测试了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_D70(): pass

    label('loc_D70')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0xD74
@scena.Code('func_03_D74')
def func_03_D74():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_E5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DDD',
    )

    ChrTalk(
        0x0009,
        (
            '#0541270012V#103F怎么？这么关心\n',
            '我的发明吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270013V#101F呵呵，敬请期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E5B')

    def _loc_DDD(): pass

    label('loc_DDD')

    ChrTalk(
        0x0009,
        (
            '#0541270014V#100F调查还顺利吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270015V我这边的准备\n',
            '还要有一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270016V一旦准备妥当\n',
            '我就会联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_E5B(): pass

    label('loc_E5B')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0xE5F
@scena.Code('func_04_E5F')
def func_04_E5F():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1062',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_EDE',
    )

    ChrTalk(
        0x000A,
        (
            '#0070890022V#560F这装置一定会\n',
            '起作用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890023V我们会加快速度的，\n',
            '请再稍微等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6A')

    def _loc_EDE(): pass

    label('loc_EDE')

    ChrTalk(
        0x000A,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890024V现在在准备的装置\n',
            '我想一定能帮上忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890025V我们会加快速度的，\n',
            '请再稍微等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F6A(): pass

    label('loc_F6A')

    Jump('loc_1062')

    def _loc_F6D(): pass

    label('loc_F6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FD8',
    )

    ChrTalk(
        0x000A,
        (
            '#0070890026V#060F这个装置\n',
            '一定会起作用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890027V我们会加快速度的，\n',
            '请再稍微等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1062')

    def _loc_FD8(): pass

    label('loc_FD8')

    ChrTalk(
        0x000A,
        (
            '#0070271311V#060F啊，姐姐是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890028V现在在准备的装置\n',
            '一定会起作用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890029V我们会加快速度的，\n',
            '请再稍微等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1062(): pass

    label('loc_1062')

    TalkEnd(0x000A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
