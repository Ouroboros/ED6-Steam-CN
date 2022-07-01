import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0901_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0901   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '小船'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0901.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x191F
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
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x10A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x10A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x10A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_118',
    )

    OP_A3(0x10F0)
    Event(0, 0x0002)

    def _loc_118(): pass

    label('loc_118')

    Return()

# id: 0x0001 offset: 0x119
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x11A
@scena.Code('ReInit')
def ReInit():
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
        'loc_131',
    )

    Call(0, 0x0005)
    Call(0, 0x0006)

    def _loc_131(): pass

    label('loc_131')

    FadeOut(0, 0, -1)
    OP_76(0x00FF, 0x00000000, 0x0001, 0x00000002, 0x00000001, 0x00000000, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 0x00000000, 0xFFFFFFFE, 0x00000000, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, 0x00000000, 0xFFFFFFFF, 0x00000000, 0x00, 0x00)
    OP_6D(1210, -2990, -360, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(271000, 0)
    OP_6E(370, 0)
    OP_A1(0x0008, 0x0000)
    SetChrPos(0x0008, -28690, -2850, 20660, 305)
    Yield()
    SetChrBattleFlags(0x0101, 0x0020)
    SetChrBattleFlags(0x0109, 0x0020)
    SetChrBattleFlags(0x00F8, 0x0020)
    SetChrBattleFlags(0x00F9, 0x0020)
    OP_89(0x0101, -27480, -2750, 20350, 125)
    OP_89(0x0109, -27880, -2750, 19880, 125)
    OP_89(0x00F8, -28750, -2750, 21200, 125)
    OP_89(0x00F9, -29110, -2750, 20650, 125)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0109, 0x0040)
    SetChrFlags(0x00F8, 0x0040)
    SetChrFlags(0x00F9, 0x0040)
    ClearChrFlags(0x0101, 0x0001)
    ClearChrFlags(0x0109, 0x0001)
    ClearChrFlags(0x00F8, 0x0001)
    ClearChrFlags(0x00F9, 0x0001)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0109, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0109, 7)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_280',
    )

    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 1)

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_298',
    )

    SetChrSubChip(0x0106, 0)
    SetChrChipByIndex(0x0106, 2)

    def _loc_298(): pass

    label('loc_298')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B0',
    )

    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0104, 3)

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C8',
    )

    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0105, 4)

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E0',
    )

    SetChrSubChip(0x0107, 0)
    SetChrChipByIndex(0x0107, 5)

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F8',
    )

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 6)

    def _loc_2F8(): pass

    label('loc_2F8')

    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 301)
    OP_70(0x0000, 0x00000168)
    LoadEffect(0x01, 'map\\\\mp013_00.eff')
    LoadEffect(0x02, 'map\\\\mp013_01.eff')
    PlayEffect(0x01, 0x01, 0x0008, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x0008, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01CC, 0x00, 0x64)
    OP_22(0x00DA, 0x01, 0x4B)
    Sleep(2000)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        OP_8F(0x00FE, 0, -2850, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_03B6)

    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_03DB')
    def lambda_03DB():
        OP_6B(3200, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03DB)

    WaitForThreadExit(0x0008, 0x0000)
    TerminateThread(0x0101, 0x00)
    Fade(1000)
    OP_6D(330, -2830, -510, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(180000, 0)
    OP_6E(229, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0109, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    OP_89(0x0101, 1050, -2750, -300, 125)
    OP_89(0x0109, 620, -2750, -850, 125)
    OP_89(0x00F8, -50, -2750, 450, 125)
    OP_89(0x00F9, -500, -2750, 0, 125)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320958V#1003F#6P呼……好安静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320959V#1002F差不多快能\n',
            '看见对岸了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04EC')
    def lambda_04EC():
        OP_67(0, 6500, -10000, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04EC)

    @scena.Lambda('lambda_0504')
    def lambda_0504():
        OP_6B(3050, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0504)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_575',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320960V#074F#4P嗯……\n',
            '方向应该是对的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320961V#070F没必要那么着急吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320962V#053F#4P方向应该是对的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320963V#050F别着急，继续前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_5D5(): pass

    label('loc_5D5')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_63A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320964V#026F#4P方向应该是对的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320965V#020F别着急，\n',
            '继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_63A(): pass

    label('loc_63A')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320966V#035F#4P根据地图，\n',
            '方向应该没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320967V#030F别着急，继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_6A7(): pass

    label('loc_6A7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_705',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320968V#542F#4P方向应该是对的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320969V继续前进的话就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_705(): pass

    label('loc_705')

    Sleep(100)

    SetChrSubChip(0x0109, 2)
    Sleep(400)

    ChrTalk(
        0x0109,
        (
            '#0180320970V#1062F#6P嗯～话说回来，\n',
            '今晚的月色可真美啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320971V#1061F在这种夜晚，\n',
            '本该带着女朋友来\n',
            '约会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0101, 2)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320972V#1007F#6P又说这么悠哉的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320973V#1008F不过想不到\n',
            '凯文先生你有女朋友啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0109, 1)
    Sleep(400)

    ChrTalk(
        0x0109,
        (
            '#0180320974V#1071F#5P哼，我在大陆各地的城市里\n',
            '可都有一位候补恋人哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320975V#1028F#6P候补恋人也就等于\n',
            '没有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180320976V#1068F#5P啊唔……\n',
            '再让我多吹嘘一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F6',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320977V#045F#4P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F6(): pass

    label('loc_8F6')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_926',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320978V#061F#4P嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_926(): pass

    label('loc_926')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_958',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320979V#027F#4P哎呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_958(): pass

    label('loc_958')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_999',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320980V#035F#4P呵呵，你的\n',
            '修行还不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_999(): pass

    label('loc_999')

    ChrTalk(
        0x0101,
        (
            '#0010320981V#1015F#6P……不过凯文先生你\n',
            '为什么是一个人单独行动呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320982V『星杯骑士团』\n',
            '真有这么欠缺人手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180320983V#1067F#5P总之这次是因为有\n',
            '各种各样的原因……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320984V#1065F于是最后就派遣\n',
            '我一个人来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320985V#1060F视情况需要，\n',
            '其他人也有可能来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320986V#1004F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320987V#1015F嗯，你以前说过\n',
            '『星杯骑士团』的工作\n',
            '是回收古代遗物对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180320988V#1060F#5P确切地说是调查、管理、回收。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320989V其中回收的对象\n',
            '主要是个人所持有的古代遗物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320990V#1065F因为教会严格禁止\n',
            '个人随意地持有\n',
            '能够运作的古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C2F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320991V#064F#4P请问请问，为什么\n',
            '必须要进行管制呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C69')

    def _loc_C2F(): pass

    label('loc_C2F')

    ChrTalk(
        0x0101,
        (
            '#0010320992V#1004F#6P不过，为什么\n',
            '必须要进行管制呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C69(): pass

    label('loc_C69')

    ChrTalk(
        0x0109,
        (
            '#0180320993V#1063F#5P古代遗物的种类\n',
            '虽然是五花八门……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320994V但却没有人知道\n',
            '它们的运作原理如何。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320995V#1065F因此，依使用方式的不同，\n',
            '也有可能发挥出惊人的能量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320996V#1067F那种东西如果让个人持有的话，\n',
            '你觉得会发生什么样的情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DAA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320997V#063F#4P啊……\n',
            '到底会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE0')

    def _loc_DAA(): pass

    label('loc_DAA')

    ChrTalk(
        0x0101,
        (
            '#0010320998V#1015F#6P嗯、嗯……\n',
            '到底会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE0(): pass

    label('loc_DE0')

    ChrTalk(
        0x0109,
        (
            '#0180320999V#1063F#5P他们大多会被迷惑住。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321000V因无法抵抗这种力量的诱惑\n',
            '而做出不正当的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E80',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321001V#065F#4P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E80(): pass

    label('loc_E80')

    ChrTalk(
        0x0101,
        (
            '#0010321002V#1002F#6P这、这是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321003V#1065F#5P很遗憾，历史就是\n',
            '这么证明给我们看的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321004V#1063F艾丝蒂尔你们也\n',
            '知道戴尔蒙市长的事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FDA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321005V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060321006V#049F#4P的确，那时候的市长\n',
            '让人感觉十分地残忍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321007V与其说是被操纵了，倒不如说\n',
            '是已经无法控制自己了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_107B')

    def _loc_FDA(): pass

    label('loc_FDA')

    ChrTalk(
        0x0101,
        (
            '#0010321008V#1020F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321009V#1007F的确，那时候的市长\n',
            '让人感觉十分地残忍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321010V与被操纵了的空贼头目不同，\n',
            '好像是自己无法控制自己了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_107B(): pass

    label('loc_107B')

    ChrTalk(
        0x0109,
        (
            '#0180321011V#1065F#5P人一旦拥有了绝对的力量\n',
            '就会产生一种扭曲的自信，\n',
            '使之丧失自制能力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321012V#1060F因此，『星杯骑士团』的使命\n',
            '就是为了防止这样的事情再次发生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321013V#1068F当然，不能完全说得这么好听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321014V#1004F#6P是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1328',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321015V#035F#4P呵，教会也有着\n',
            '各种不为人知的隐情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321016V#030F好像有时候\n',
            '也会允许个人\n',
            '持有古代遗物吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1244',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321017V#027F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1244(): pass

    label('loc_1244')

    ChrTalk(
        0x0109,
        (
            '#0180321018V#1064F#5P……你知道的还真多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321019V#1071F不过对于这件事\n',
            '我无可奉告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321020V因为我有保守秘密的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040321021V#035F#4P呵呵，这也是当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321022V#1019F#6P多少有点可疑啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13BE')

    def _loc_1328(): pass

    label('loc_1328')

    ChrTalk(
        0x0109,
        (
            '#0180321023V#1062F#5P不过游击士协会\n',
            '也有不可公开的事情吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321024V这都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321025V#1007F#6P嗯、嗯……\n',
            '这一点的确无法否认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_13BE(): pass

    label('loc_13BE')

    @scena.Lambda('lambda_13C4')
    def lambda_13C4():
        OP_6E(315, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13C4)

    CreateThread(0x0008, 0x02, 0x00, 0x0004)
    Sleep(1000)

    OP_12(0x000003E8, 0x0000EA60, 0x00001F40)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(700)

    OP_20(0x000007D0)
    OP_82(0x80, 0x02)
    OP_82(0x81, 0x02)
    OP_82(0x82, 0x02)
    Sleep(100)

    SetChrSubChip(0x0109, 0)
    Sleep(100)

    SetChrSubChip(0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010321026V#1005F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14E8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321027V#022F#4P看来我们已经接近\n',
            '敌人的据点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161D')

    def _loc_14E8(): pass

    label('loc_14E8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1534',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321028V#057F#4P看来我们已经接近\n',
            '敌人的据点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161D')

    def _loc_1534(): pass

    label('loc_1534')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1580',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321029V#072F#4P看来我们已经接近\n',
            '敌人的据点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161D')

    def _loc_1580(): pass

    label('loc_1580')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15D0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321030V#065F#4P一接近『结社』的据点\n',
            '就会产生浓雾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161D')

    def _loc_15D0(): pass

    label('loc_15D0')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_161D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321031V#042F#4P看来我们已经接近\n',
            '『结社』的据点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_161D(): pass

    label('loc_161D')

    Sleep(500)

    OP_21()
    OP_1D(0x7D)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180321032V#1063F#5P那么，现在看来\n',
            '只能一直前进了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321033V#1002F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321034V敌人也有可能设下埋伏，\n',
            '提高警觉小心前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    CreateThread(0x0008, 0x03, 0x00, 0x0003)
    OP_12(0x000003E8, 0x00007530, 0x000007D0)

    @scena.Lambda('lambda_16DD')
    def lambda_16DD():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16DD)

    Sleep(500)

    @scena.Lambda('lambda_16F8')
    def lambda_16F8():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16F8)

    Sleep(400)

    @scena.Lambda('lambda_1713')
    def lambda_1713():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1713)

    Sleep(300)

    @scena.Lambda('lambda_172E')
    def lambda_172E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_172E)

    Sleep(200)

    @scena.Lambda('lambda_1749')
    def lambda_1749():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1749)

    Sleep(100)

    @scena.Lambda('lambda_1764')
    def lambda_1764():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00004650, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1764)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_82(0x00, 0x02)
    SetMapFlags(0x02000000)
    SetMapFlags(0x00100000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x179E
@scena.Code('func_03_179E')
def func_03_179E():
    OP_72(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 241)
    OP_70(0x0000, 0x0000015E)
    OP_73(0x0000)
    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 301)
    OP_70(0x0000, 0x00000168)

    Return()

# id: 0x0004 offset: 0x17D4
@scena.Code('func_04_17D4')
def func_04_17D4():
    OP_22(0x01C3, 0x01, 0x64)
    Sleep(3000)

    OP_24(0x01C3, 0x5A)
    Sleep(200)

    OP_24(0x01C3, 0x5A)
    Sleep(200)

    OP_24(0x01C3, 0x50)
    Sleep(200)

    OP_24(0x01C3, 0x46)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    Sleep(200)

    OP_23(0x01C3)

    Return()

# id: 0x0005 offset: 0x182A
@scena.Code('func_05_182A')
def func_05_182A():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_18A7'),
        (0x00000001, 'loc_18AD'),
        (-1, 'loc_18B3'),
    )

    def _loc_18A7(): pass

    label('loc_18A7')

    OP_A2(0x1200)

    Jump('loc_18B3')

    def _loc_18AD(): pass

    label('loc_18AD')

    OP_A2(0x1201)

    Jump('loc_18B3')

    def _loc_18B3(): pass

    label('loc_18B3')

    Return()

# id: 0x0006 offset: 0x18B4
@scena.Code('func_06_18B4')
def func_06_18B4():
    ClearMapFlags(0x00000001)
    OP_6D(15460, -2990, 171130, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0008,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
