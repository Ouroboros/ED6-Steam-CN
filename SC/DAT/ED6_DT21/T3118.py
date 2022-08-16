import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3118_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3118   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3118.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0001
    header.entryFunction  = 0x0000
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3118_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '米妮亚姆医生',
            x                   = -1410,
            z                   = 0,
            y                   = 6690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = -5510,
            z                   = 0,
            y                   = -3140,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = -5510,
            z                   = 0,
            y                   = -3140,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -5510,
            triggerZ            = 0,
            triggerY            = -3140,
            triggerRange        = 1000,
            actorX              = -5510,
            actorZ              = 500,
            actorY              = -3140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x13E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_15B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_158',
    )

    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x00, func_02_19F)

    def _loc_158(): pass

    label('loc_158')

    Jump('loc_16E')

    def _loc_15B(): pass

    label('loc_15B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_16E',
    )

    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x00, func_02_19F)

    def _loc_16E(): pass

    label('loc_16E')

    Return()

# id: 0x0001 offset: 0x16F
@scena.Code('func_01_16F')
def func_01_16F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A',
    )

    OP_6F(0x0000, 29)
    OP_72(0x0000, 0x0010)
    OP_79(0xFF, 0x0002)
    OP_7A(0x07, 0x0002)
    OP_7B()
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)

    def _loc_19A(): pass

    label('loc_19A')

    OP_64(0x00, 0x0001)

    Return()

# id: 0x0002 offset: 0x19F
@scena.Code('func_02_19F')
def func_02_19F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1FF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0400)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E5',
    )

    OP_8D(0x00FE, -3860, -2270, -5240, -3760, 1000)

    Jump('loc_1FC')

    def _loc_1E5(): pass

    label('loc_1E5')

    OP_8D(0x00FE, -6290, -6030, -3150, 520, 1000)

    def _loc_1FC(): pass

    label('loc_1FC')

    Jump('func_02_19F')

    def _loc_1FF(): pass

    label('loc_1FF')

    Return()

# id: 0x0003 offset: 0x200
@scena.Code('func_03_200')
def func_03_200():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_599',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 3, 0x20D3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B2',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_295',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，诸位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有提妲也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F米妮亚姆医生，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C9')

    def _loc_295(): pass

    label('loc_295')

    ChrTalk(
        0x00FE,
        (
            '哎呀，诸位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C9(): pass

    label('loc_2C9')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你看起来很有精神，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F米妮亚姆医生也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F不过你的工作\n',
            '好像很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，我刚检查了\n',
            '医药品的储备情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关键的时候\n',
            '没有药可就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现状运输手段\n',
            '也很匮乏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时只能控制一下\n',
            '药品的使用量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以你们也要\n',
            '小心一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果受重伤的话\n',
            '我可饶不了你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_475',
    )

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……我会注意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……听到吗？阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#552F为什么问我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A9')

    def _loc_475(): pass

    label('loc_475')

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F我们会充分注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A9(): pass

    label('loc_4A9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x041A, 3, 0x20D3))

    Jump('loc_596')

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_554',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_509',
    )

    ChrTalk(
        0x00FE,
        (
            '暂时只能控制一下\n',
            '药品的使用量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也要\n',
            '也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_551')

    def _loc_509(): pass

    label('loc_509')

    ChrTalk(
        0x00FE,
        (
            '总觉得好久\n',
            '没见到安东尼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，这孩子之前\n',
            '究竟去了哪儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_551(): pass

    label('loc_551')

    Jump('loc_596')

    def _loc_554(): pass

    label('loc_554')

    ChrTalk(
        0x00FE,
        (
            '暂时只能控制一下\n',
            '药品的使用量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也要\n',
            '多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_596(): pass

    label('loc_596')

    Jump('loc_108F')

    def _loc_599(): pass

    label('loc_599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 6, 0x142E)),
            Expr.Return,
        ),
        'loc_A6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_70E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_658',
    )

    ChrTalk(
        0x00FE,
        (
            '七耀教会的神父\n',
            '现在也在开发着新药哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他们为什么能开发新药\n',
            '到现在仍然是个疑问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我看了那篇论文以后就明白了。\n',
            '总之是有很强的人在里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70B')

    def _loc_658(): pass

    label('loc_658')

    ChrTalk(
        0x00FE,
        (
            '最近在一本医学杂志上\n',
            '读了神父写的论文。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在是写得太棒了。\n',
            '我都有点受打击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅了解教会的传统医疗，\n',
            '连现代医学也懂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有机会真想和作者\n',
            '迪拜恩神父聊聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_70B(): pass

    label('loc_70B')

    Jump('loc_A22')

    def _loc_70E(): pass

    label('loc_70E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_828',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_77D',
    )

    ChrTalk(
        0x00FE,
        (
            '我最近的研究课题\n',
            '就是做教会处方的药的分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '整理一下知识的话\n',
            '一定能发现一些什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_825')

    def _loc_77D(): pass

    label('loc_77D')

    ChrTalk(
        0x00FE,
        (
            '我最近的研究课题\n',
            '就是做教会处方的药的分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果已经把那种治肩酸的药的\n',
            '药理结构都已经掌握了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然可能只是一小步，\n',
            '不过积累下去的话就能找到突破口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_825(): pass

    label('loc_825')

    Jump('loc_A22')

    def _loc_828(): pass

    label('loc_828')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_97A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8C4',
    )

    ChrTalk(
        0x00FE,
        (
            '医学者赖以立足的\n',
            '近代医学还历史尚浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然在外科领域有了成果，\n',
            '不过药学的知识还不及教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他们积累了\n',
            '一千年以上的经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_977')

    def _loc_8C4(): pass

    label('loc_8C4')

    ChrTalk(
        0x00FE,
        (
            '阿加特能够得救也是\n',
            '因为有了七耀教会的药吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这药很令人感兴趣，\n',
            '所以我也试着分析了一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是不明白\n',
            '为什么会起效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，近代医学的力量\n',
            '还不过如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_977(): pass

    label('loc_977')

    Jump('loc_A22')

    def _loc_97A(): pass

    label('loc_97A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_A22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9DD',
    )

    ChrTalk(
        0x00FE,
        (
            '在中央工房的研究室里\n',
            '也有危险的药品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果瓶子碎了的话\n',
            '就不好收拾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A22')

    def _loc_9DD(): pass

    label('loc_9DD')

    ChrTalk(
        0x00FE,
        (
            '没有人因\n',
            '地震受伤呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，客人\n',
            '摇晃得不厉害真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_A22(): pass

    label('loc_A22')

    Jump('loc_A6B')

    def _loc_A25(): pass

    label('loc_A25')

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话\n',
            '你们随时都可以来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一般都在\n',
            '这个房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_A6B(): pass

    label('loc_A6B')

    Jump('loc_108F')

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D2A',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，米妮亚姆医生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F那时候太\n',
            '麻烦您，真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F嗯，受你照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '阿加特。\n',
            '你看起来很有精神，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来身体的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F没问题。\n',
            '托你的福，完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真是太好了。\n',
            '好像也没有后遗症……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，了不起的恢复能力。\n',
            '到底是以身体作为资本的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，这就是阿加特。\n',
            '只有体力是没话说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C3A',
    )

    ChrTalk(
        0x0107,
        (
            '#067F哎，嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C3A(): pass

    label('loc_C3A')

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话\n',
            '随时可以到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，那种伤势\n',
            '还是不希望再见到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F嗯，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我也不想再受\n',
            '那样的伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，你可别忘记这话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要小心\n',
            '继续努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么再见了，医生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1089')

    def _loc_D2A(): pass

    label('loc_D2A')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，米妮亚姆医生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F那时候真是\n',
            '还麻烦您，真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC8',
    )

    ChrTalk(
        0x0107,
        (
            '#562F真、真的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC8(): pass

    label('loc_DC8')

    ChrTalk(
        0x00FE,
        (
            '不，我什么也没做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要感谢的话\n',
            '就感谢教区长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么……\n',
            '阿加特还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，没问题。\n',
            '看上去已经完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，了不起的恢复能力。\n',
            '到底是以身体作为资本的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，这就是阿加特。\n',
            '只有体力是没话说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EFA',
    )

    ChrTalk(
        0x0107,
        (
            '#067F哎，嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EFA(): pass

    label('loc_EFA')

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话\n',
            '你们随时可以过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，那种伤势\n',
            '还是不希望再见到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是啊……\n',
            '得小心谨慎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '无论怎样的工作\n',
            '都隐藏着危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F嗯，就像艾丝蒂尔说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为了防备看不见的威胁\n',
            '要经常把感觉磨练的敏感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F卡西乌斯老师也经常说\n',
            '这是游击士的心得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，请一定不要忘记那些话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '今后也要小心\n',
            '继续努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么再见了，医生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1089(): pass

    label('loc_1089')

    SetScenaFlags(ScenaFlag(0x0285, 6, 0x142E))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_108F(): pass

    label('loc_108F')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1093
@scena.Code('func_04_1093')
def func_04_1093():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_10B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_10B3',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B3(): pass

    label('loc_10B3')

    Jump('loc_10C5')

    def _loc_10B6(): pass

    label('loc_10B6')

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_10C5(): pass

    label('loc_10C5')

    TalkEnd(0x0009)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
