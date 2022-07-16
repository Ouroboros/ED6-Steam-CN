import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '希德少校'),
    TXT(0x02, '卫兵'),
    TXT(0x03, '卫兵'),
    TXT(0x04, '士兵塞缪尔'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3100.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2A3F
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
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3340,
            z                   = 0,
            y                   = -4720,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -6310,
            y           = -1000,
            z           = -4980,
            range       = 6020,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFDAC6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 5480,
            y           = -1000,
            z           = -41450,
            range       = -5800,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFF61C2,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -5300,
            y           = -1000,
            z           = -7680,
            range       = 5340,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE94E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6000,
            triggerZ            = 0,
            triggerY            = -45540,
            triggerRange        = 1500,
            actorX              = 6000,
            actorZ              = 1500,
            actorY              = -45540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1CA'),
        (-1, 'loc_1E0'),
    )

    def _loc_1CA(): pass

    label('loc_1CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 3, 0x55B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DD',
    )

    SetScenaFlags(ScenaFlag(0x00AB, 3, 0x55B))
    Event(0, 0x0004)

    def _loc_1DD(): pass

    label('loc_1DD')

    Jump('loc_1E0')

    def _loc_1E0(): pass

    label('loc_1E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1EA',
    )

    Jump('loc_22A')

    def _loc_1EA(): pass

    label('loc_1EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_205',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0010)
    SetChrDirection(0x000B, 90, 0)

    Jump('loc_22A')

    def _loc_205(): pass

    label('loc_205')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_20F',
    )

    Jump('loc_22A')

    def _loc_20F(): pass

    label('loc_20F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_21E',
    )

    ClearChrFlags(0x000B, 0x0080)

    Jump('loc_22A')

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_22A',
    )

    ClearChrFlags(0x000B, 0x0080)

    def _loc_22A(): pass

    label('loc_22A')

    Return()

# id: 0x0001 offset: 0x22B
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 4, 0x55C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_243',
    )

    OP_6F(0x0000, 310)

    def _loc_243(): pass

    label('loc_243')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Return,
        ),
        'loc_253',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_253(): pass

    label('loc_253')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_267',
    )

    OP_28(0x002A, 0x01, 0x4000)

    def _loc_267(): pass

    label('loc_267')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x26D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_282',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_282(): pass

    label('loc_282')

    Return()

# id: 0x0003 offset: 0x283
@scena.Code('func_03_283')
def func_03_283():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_46D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_316',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了希德少校的名誉，\n',
            '还是拒绝了好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '少校是个好人，也很聪明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过……\n',
            '他心太软了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_46A')

    def _loc_316(): pass

    label('loc_316')

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '说起来，希德少校也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让情报部的那些家伙们\n',
            '随便使唤来使唤去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为人老实虽然好，\n',
            '可是也要看对象是谁啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(400)

    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '哇、哇～！\n',
            '什么时候来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平、平民\n',
            '禁止进入这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快回去！\n',
            '要不然就把你们抓起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 180, 0)
    OP_4B(0x00FE, 255)
    ClearMapFlags(0x00000080)

    def _loc_46A(): pass

    label('loc_46A')

    Jump('loc_6CD')

    def _loc_46D(): pass

    label('loc_46D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_627',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4D5',
    )

    ChrTalk(
        0x00FE,
        (
            '……嗯？\n',
            '你、你们还在这里吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不赶快离开的话，\n',
            '这次真的要把你们抓起来哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_621')

    def _loc_4D5(): pass

    label('loc_4D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5C2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '怎么了，\n',
            '你们就这么想被逮捕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不是在威胁你们。\n',
            '因为现在有情报部的部队\n',
            '驻扎在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咳咳……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总、总之，\n',
            '你们赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_621')

    def _loc_5C2(): pass

    label('loc_5C2')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这里是王国军的据点\n',
            '雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '普通老百姓\n',
            '是不能进去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请你们赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_621(): pass

    label('loc_621')

    TalkEnd(0x00FE)

    Jump('loc_6CD')

    def _loc_627(): pass

    label('loc_627')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6CD',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_66B',
    )

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赖在这里也没有用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CA')

    def _loc_66B(): pass

    label('loc_66B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这里是王国军的据点\n',
            '雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '普通老百姓\n',
            '是不能进去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请你们赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CA(): pass

    label('loc_6CA')

    TalkEnd(0x00FE)

    def _loc_6CD(): pass

    label('loc_6CD')

    Return()

# id: 0x0004 offset: 0x6CE
@scena.Code('func_04_6CE')
def func_04_6CE():
    EventBegin(0x00)
    SetChrPos(0x0101, -50, 0, -57100, 0)
    SetChrPos(0x0102, -1380, 0, -57730, 0)
    CameraMove(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x000493E0, 0x00001F40)

    @scena.Lambda('lambda_0742')
    def lambda_0742():
        CameraMove(1220, 250, -12050, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0742)

    @scena.Lambda('lambda_075A')
    def lambda_075A():
        OP_67(0, 5140, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_075A)

    @scena.Lambda('lambda_0772')
    def lambda_0772():
        CameraSetDistance(8860, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0772)

    @scena.Lambda('lambda_0782')
    def lambda_0782():
        OP_6C(77000, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0782)

    Sleep(9000)

    Fade(1000)
    OP_12(0x00009470, 0x0001FBD0, 0x00000000)
    CameraMove(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090158V#004F唔哇～……\n',
            '这么大的军事基地啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090159V约修亚，你看！\n',
            '有那个哈肯大门两倍大吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090160V#012F是啊……\n',
            '说不定是有好几倍哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090161V这里在十年前的战争中不但没有陷落，\n',
            '反而成为了王国反攻作战的根据地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090162V#006F原来是这样啊……\n',
            '不过，现在可不是赞赏的时候吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090163V总之赶快去门口，\n',
            '把这里的负责人叫出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090164V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090165V#004F#2P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090166V#010F没什么……\n',
            '只是觉得你越来越勇往直前了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090167V不愧是父亲的女儿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090168V#007F#2P不怕跟你说，\n',
            '其实我也有点紧张的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090169V只不过我想这里应该不会有\n',
            '比那个摩尔根将军更加可怕的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090170V#019F哈哈，大概是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090171V#013F摩尔根将军……\n',
            '现在还留守在哈肯大门吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xAAF
@scena.Code('func_05_AAF')
def func_05_AAF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 4, 0x55C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 3, 0x55B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2726',
    )

    SetScenaFlags(ScenaFlag(0x00AB, 4, 0x55C))
    OP_28(0x0043, 0x01, 0x0002)
    OP_28(0x0043, 0x01, 0x0004)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -730, 250, -10440, 0)
    SetChrPos(0x0102, 580, 250, -10420, 0)
    CameraMove(420, 1480, -5420, 0)
    OP_67(0, 6320, -20350, 0)
    CameraSetDistance(1000, 0)
    OP_6E(611, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090172V#004F咦，没人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090173V#012F奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090174V按照军队的规定，\n',
            '这里应该会有门卫站岗的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090175V',
            (TxtCtl.SetColor, 0x5),
            '……你们是来做什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090176V#004F哎，咦……\n',
            '哪里传出来的声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090177V#012F大概是那边的扩音器。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090178V这里是雷斯顿要塞，\n',
            '利贝尔王国军的总司令部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090179V雷斯顿要塞是军事禁区，\n',
            '不是你们平民能靠近的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090180V抱歉，麻烦你们马上离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090181V#505F（真、真叫人觉得不爽啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090182V#015F（嗯……\n',
            '　看来这里的戒备相当严密啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090183V喂喂！\n',
            '你们听到了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090184V#006F不好意思，\n',
            '我们两个不是普通的平民。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090185V我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090186V#010F关于中央工房的袭击事件，\n',
            '我们有些问题想当面请教一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090187V能让我们见见你们的负责人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090188V游击士协会……\n',
            '你们两个是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090189V#006F要是不信的话，\n',
            '麻烦你看一下这个胸章。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090190V这个这个，看到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090191V…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090192V……确认完毕，\n',
            '看来你们的确是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090193V不过很不凑巧，\n',
            '这个要塞的负责人刚好外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090194V可以的话麻烦改日再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090195V#505F负责人不在……\n',
            '总觉得这是敷衍别人的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090196V#010F那么能让我们见见情报部的人吗？\n',
            '任何一位都可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090197V我们有些事情要向\n',
            '理查德上校和凯诺娜上尉传达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('男性的声音')

    Talk(
        (
            '#0620090198V…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0620090199V那好，你们先等一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010090200V#007F呼……\n',
            '终于把头儿给叫出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090201V#012F嗯……但这里的戒备\n',
            '真是比想象中还要森严啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 40, 0, 3860, 180)
    SetChrPos(0x0009, -760, 160, 4180, 180)
    SetChrPos(0x000A, 900, 160, 4180, 180)
    OP_4A(0x0009, 0)
    OP_4A(0x000A, 0)
    OP_72(0x0000, 0x0010)
    OP_70(0x0000, 450)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090202V#004F哇哇……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090203V#012F好像有人来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11C3')
    def lambda_11C3():
        OP_67(0, 12570, -20350, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11C3)

    OP_6C(0, 8000)
    OP_73(0x0000)

    @scena.Lambda('lambda_11E7')
    def lambda_11E7():
        ChrWalkTo(0x00FE, -110, 210, -7300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11E7)

    Sleep(500)

    @scena.Lambda('lambda_1207')
    def lambda_1207():
        ChrWalkTo(0x00FE, -940, 170, -6360, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1207)

    @scena.Lambda('lambda_1222')
    def lambda_1222():
        ChrWalkTo(0x00FE, 790, 170, -6380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1222)

    @scena.Lambda('lambda_123D')
    def lambda_123D():
        CameraMove(-150, 190, -6720, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_123D)

    @scena.Lambda('lambda_1255')
    def lambda_1255():
        CameraSetDistance(850, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1255)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0620090204V#700F#5P非常抱歉，让你们久等了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090205V我是雷斯顿要塞的守备队长\n',
            '希德少校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090206V#006F我是游击士协会的\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090207V#010F同属游击士协会的约修亚·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090208V#702F#5P……布莱特……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090209V#004F咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090210V#703F#5P不，没……\n',
            '抱歉，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090211V#701F言归正传……\n',
            '你们来的目的是要传达有关\n',
            '中央工房袭击事件的事情对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090212V真是非常抱歉……\n',
            '情报部的所有人刚刚外出。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090213V有什么事的话，我可以代为传达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090214V#007F唔，这就麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090215V#006F（好，\n',
            '　这就试探一下他们……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '「抓到了那些袭击中央工房的犯人」\n'),
            TXT(0x01, '「查到了被绑架的拉赛尔博士的行踪」\n'),
            TXT(0x02, '「找到了犯人掳走博士时乘的飞艇的线索」\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1552'),
        (0x00000001, 'loc_16E8'),
        (0x00000002, 'loc_1880'),
        (-1, 'loc_193A'),
    )

    def _loc_1552(): pass

    label('loc_1552')

    ChrTalk(
        0x0101,
        (
            '#0010090216V#007F唉唉，我们好不容易\n',
            '抓到了那些袭击中央工房的犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0620090217V#702F#5P说、说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090218V#019F艾丝蒂尔，这太性急了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090219V我们只不过找到了一些\n',
            '犯人掳走博士时乘的飞艇的线索而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090220V#001F啊，抱歉抱歉。\n',
            '刚才不小心说错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090221V#700F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090222V#006F咦，少校。\n',
            '为什么突然沉默了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193A')

    def _loc_16E8(): pass

    label('loc_16E8')

    ChrTalk(
        0x0101,
        (
            '#0010090223V#007F唉唉，我们好不容易\n',
            '查到了被绑架的拉赛尔博士的行踪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0620090224V#702F#5P说、说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090225V#019F艾丝蒂尔，这太性急了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090226V我们只不过找到了一些\n',
            '犯人掳走博士时乘的飞艇的线索而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090227V#001F啊，抱歉抱歉。\n',
            '刚才不小心说错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090228V#700F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090229V#006F咦，少校。\n',
            '为什么突然沉默了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193A')

    def _loc_1880(): pass

    label('loc_1880')

    ChrTalk(
        0x0101,
        (
            '#0010090230V#007F唉唉，我们好不容易\n',
            '找到了犯人掳走博士时乘的飞艇的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0620090231V#702F#5P说、说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090232V#006F咦，少校。\n',
            '您怎么那么吃惊啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193A')

    def _loc_193A(): pass

    label('loc_193A')

    ChrTalk(
        0x0008,
        (
            '#0620090233V#701F#5P不，没什么……\n',
            '因为接到联络后我们也在不断搜索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090234V对了……\n',
            '是什么线索呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090235V#012F请少校看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 210, 250, -8300, 3000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '朵洛希拍的照片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0358, 1)
    ChrMoveTo(0x0102, 500, 250, -8850, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0620090236V#702F#5P这……\n',
            '不就是雷斯顿要塞吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090237V这样的照片你们是怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -600, 240, -7820, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090238V#006F哎呀哎呀。\n',
            '不要说得那么肯定嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090239V请仔细看看照片的右上角。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090240V#700F#5P右上角……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0620090241V#704F#5P这、这个是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090242V#010F这艘飞艇的轮廓和\n',
            '军队使用的警备飞艇明显不同吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090243V#507F但是却和犯人绑架博士时乘的飞艇\n',
            '一模一样哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090244V#700F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090245V#703F原来如此……\n',
            '这的确是相当奇怪的事态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090246V感谢你们的合作，\n',
            '我会尽快将此事传达情报部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090247V#004F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090248V等、等一下！\n',
            '这样说几句就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090249V#702F#5P小姐你的意思是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0101, -720, 250, -8430, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090250V#009F因、因为……\n',
            '你不觉得这照片很不可思议吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090251V为什么犯人乘坐的飞艇\n',
            '会在戒备森严的要塞上空出现？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090252V#703F#5P虽然这样说十分惭愧，\n',
            '但我们对此确实完全不知情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090253V最近这段时间\n',
            '我们一直忙于国境附近的搜索，\n',
            '所以有时候疏忽了根据地周围的警戒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090254V从飞艇飞向瓦雷利亚湖北面这点来看，\n',
            '很有可能是帝国那边的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090255V#505F是、是这样吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090256V#013F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090257V#010F还有个问题想少校回答一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090258V请问情报部的人\n',
            '现在都去了哪里执行任务呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090259V#700F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090260V#703F这是军事机密。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090261V抱歉两位，我这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F78')
    def lambda_1F78():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1F78')

    DispatchAsync2(0x0009, 0x0001, lambda_1F78)

    @scena.Lambda('lambda_1F89')
    def lambda_1F89():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1F89')

    DispatchAsync2(0x000A, 0x0001, lambda_1F89)

    SetChrDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_1FA1')
    def lambda_1FA1():
        ChrWalkTo(0x00FE, 40, 0, 3860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FA1)

    Sleep(1000)

    @scena.Lambda('lambda_1FC1')
    def lambda_1FC1():
        ChrWalkTo(0x00FE, -760, 160, 4180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FC1)

    @scena.Lambda('lambda_1FDC')
    def lambda_1FDC():
        ChrWalkTo(0x00FE, 900, 160, 4180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1FDC)

    Sleep(2000)

    @scena.Lambda('lambda_1FFC')
    def lambda_1FFC():
        OP_67(0, 18220, -20350, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FFC)

    @scena.Lambda('lambda_2014')
    def lambda_2014():
        OP_6E(489, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2014)

    Sleep(4000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090262V#009F我、我说约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090263V这么敷衍的回答，\n',
            '不就是明摆着很奇怪嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090264V#013F我知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090265V但是只要没有决定性的证据，\n',
            '我们也就没办法继续追问下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090266V#003F唔唔～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(1000)
    CameraMove(-770, 1700, -3300, 0)
    OP_67(0, 5430, -10000, 0)
    CameraSetDistance(4880, 0)
    OP_6C(339000, 0)
    OP_6E(262, 0)
    OP_72(0x0000, 0x0800)
    PlaySE(108, 0x00, 0x64)
    OP_6F(0x0000, 450)
    OP_70(0x0000, 310)
    OP_73(0x0000)
    PlaySE(154, 0x00, 0x64)
    OP_23(0x006C)
    OP_7C(0, 100, 3000, 100)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)
    Sleep(500)

    OP_71(0x0000, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010090267V#004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090268V#014F……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '希德少校',
        (
            '#0620090269V什、什么……\n',
            '怎么会在中途停下的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090270V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090271V……什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090272V那个现象又发生了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010090273V#005F（约修亚，这是……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090274V#012F（啊啊……\n',
            '　看来我们真的猜对了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrPos(0x0008, 1280, 0, 3540, 0)
    SetChrPos(0x0009, 1280, 0, 3540, 0)
    SetChrPos(0x000A, 1280, 0, 3540, 0)

    @scena.Lambda('lambda_2340')
    def lambda_2340():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2340')

    DispatchAsync2(0x0101, 0x0003, lambda_2340)

    @scena.Lambda('lambda_2351')
    def lambda_2351():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2351')

    DispatchAsync2(0x0102, 0x0003, lambda_2351)

    @scena.Lambda('lambda_2362')
    def lambda_2362():
        CameraMove(-120, 180, -6630, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2362)

    @scena.Lambda('lambda_237A')
    def lambda_237A():
        CameraSetDistance(4090, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_237A)

    @scena.Lambda('lambda_238A')
    def lambda_238A():
        ChrWalkTo(0x00FE, -200, 170, -6470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_238A)

    Sleep(500)

    @scena.Lambda('lambda_23AA')
    def lambda_23AA():
        ChrWalkTo(0x00FE, -1010, 0, -5160, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_23AA)

    Sleep(500)

    @scena.Lambda('lambda_23CA')
    def lambda_23CA():
        ChrWalkTo(0x00FE, 990, 0, -4910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_23CA)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0620090275V#701F#2P非常抱歉，\n',
            '让你们看到丢人的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090276V最近要塞大门的开关装置\n',
            '好像运作得不太好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090277V#019F原来如此，那还真是不妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090278V#006F如果情况很糟的话，\n',
            '就请中央工房的人来修理一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090279V像拉赛尔博士那样厉害的人，\n',
            '肯定能马上为你们修好的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090280V#701F#2P嗯、嗯，我们会考虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090281V#704F在装置修好之前，\n',
            '你们在这里警戒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090282V不许随便让普通平民靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#4190090283V是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_259B')
    def lambda_259B():
        ChrWalkTo(0x00FE, -3500, 0, -4840, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_259B)

    @scena.Lambda('lambda_25B6')
    def lambda_25B6():
        SetChrDirection(0x00FE, 180, 400)
        Yield()

        Jump('lambda_25B6')

    DispatchAsync2(0x0009, 0x0001, lambda_25B6)

    ChrTalk(
        0x000A,
        (
            '#2490090284V明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_25DA')
    def lambda_25DA():
        ChrWalkTo(0x00FE, 3750, 0, -5150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_25DA)

    @scena.Lambda('lambda_25F5')
    def lambda_25F5():
        SetChrDirection(0x00FE, 180, 400)
        Yield()

        Jump('lambda_25F5')

    DispatchAsync2(0x000A, 0x0001, lambda_25F5)

    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090285V#701F#2P那就这样了，\n',
            '你们也尽快回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090286V关于那张要塞的照片，\n',
            '我一定会代为转交情报部的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090287V我这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_269C')
    def lambda_269C():
        CameraMove(-220, 250, -8550, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_269C)

    @scena.Lambda('lambda_26B4')
    def lambda_26B4():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_26B4)

    @scena.Lambda('lambda_26CC')
    def lambda_26CC():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_26CC)

    @scena.Lambda('lambda_26DC')
    def lambda_26DC():
        CameraSetDistance(2800, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_26DC)

    @scena.Lambda('lambda_26EC')
    def lambda_26EC():
        ChrWalkTo(0x00FE, 1260, 250, 3400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_26EC)

    WaitForThreadExit(0x0000, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    EventEnd(0x00)
    OP_85(0x0009)
    OP_85(0x000A)
    OP_4B(0x0009, 0)
    OP_4B(0x000A, 0)

    def _loc_2726(): pass

    label('loc_2726')

    Return()

# id: 0x0006 offset: 0x2727
@scena.Code('func_06_2727')
def func_06_2727():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 4, 0x55C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_292B',
    )

    SetScenaFlags(ScenaFlag(0x00AB, 5, 0x55D))
    OP_28(0x0043, 0x01, 0x0008)
    OP_28(0x0043, 0x01, 0x0010)
    EventBegin(0x00)
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090288V#002F真是不敢相信啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090289V刚才的果然是那个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090290V#015F嗯……\n',
            '应该就是那个现象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090291V#505F这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090292V#005F难道拉赛尔博士\n',
            '被捉到这个要塞里来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090293V#012F（小声点，艾丝蒂尔……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090294V（在这种地方\n',
            '　还是不要把那件事说出来为好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090295V#004F（明、明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090296V#013F（总之还是先回蔡斯，\n',
            '　然后和雾香小姐商量一下吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090297V（可以的话……\n',
            '　最好把玛多克工房长也请过来。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3120._SN', 100, 0, 0)
    IdleLoop()

    def _loc_292B(): pass

    label('loc_292B')

    Return()

# id: 0x0007 offset: 0x292C
@scena.Code('func_07_292C')
def func_07_292C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 4, 0x55C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29D0',
    )

    EventBegin(0x01)
    OP_4A(0x0009, 0)
    OP_4A(0x000A, 0)
    ChrTurnDirection(0x0009, 0x0000, 0)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ChrTalk(
        0x0009,
        (
            '#4190090298V你应该知道吧，\n',
            '这里禁止闲杂人等进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490090299V你们赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetChrDirection(0x0009, 180, 0)
    SetChrDirection(0x000A, 180, 0)
    OP_4B(0x0009, 0)
    OP_4B(0x000A, 0)

    def _loc_29D0(): pass

    label('loc_29D0')

    Return()

# id: 0x0008 offset: 0x29D1
@scena.Code('func_08_29D1')
def func_08_29D1():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　警告！　　　　\n',
            '军队重地，严禁拍摄',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
