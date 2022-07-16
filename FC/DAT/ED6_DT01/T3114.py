import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3114_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3114   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3114.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3114._SN', 'ED6_DT01/T3114_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE3E
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -118000,
            y           = -1000,
            z           = 23400,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -118000,
            y           = -1000,
            z           = 223400,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -118000,
            y           = -1000,
            z           = 423400,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -106990,
            y           = -1000,
            z           = -550,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -107140,
            y           = 0,
            z           = -340,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -119480,
            y           = 0,
            z           = 6960,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = -107010,
            y           = 0,
            z           = 199500,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = -119590,
            y           = 0,
            z           = 206950,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -106990,
            y           = 0,
            z           = 399440,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -119440,
            y           = 0,
            z           = 406910,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10005 offset: 0x1E8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -113730,
            triggerZ            = 0,
            triggerY            = 22590,
            triggerRange        = 1200,
            actorX              = -113730,
            actorZ              = 0,
            actorY              = 22590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -106980,
            triggerZ            = 0,
            triggerY            = -20,
            triggerRange        = 800,
            actorX              = -106980,
            actorZ              = 1000,
            actorY              = -20,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -118040,
            triggerZ            = 0,
            triggerY            = 24100,
            triggerRange        = 800,
            actorX              = -118040,
            actorZ              = 1000,
            actorY              = 24100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -117980,
            triggerZ            = 0,
            triggerY            = 224050,
            triggerRange        = 800,
            actorX              = -117980,
            actorZ              = 1000,
            actorY              = 224050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -117970,
            triggerZ            = 0,
            triggerY            = 424010,
            triggerRange        = 800,
            actorX              = -117970,
            actorZ              = 1000,
            actorY              = 424010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x29C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2AA',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_2AA(): pass

    label('loc_2AA')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2BE'),
        (0x0000006A, 'loc_2BE'),
        (0x00000070, 'loc_2BE'),
        (-1, 'loc_2C6'),
    )

    def _loc_2BE(): pass

    label('loc_2BE')

    PlaySE(14, 0x00, 0x64)

    Jump('loc_2C6')

    def _loc_2C6(): pass

    label('loc_2C6')

    Return()

# id: 0x0001 offset: 0x2C7
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_30C')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F7',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_30C')

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_30C(): pass

    label('loc_30C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 5, 0x50D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31C',
    )

    OP_72(0x0002, 0x0010)

    Jump('loc_320')

    def _loc_31C(): pass

    label('loc_31C')

    OP_64(0x01, 0x0001)

    def _loc_320(): pass

    label('loc_320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_49C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_3DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 1, 0x549)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D8',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -113730, 0, 22590, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_3DC')

    def _loc_3D8(): pass

    label('loc_3D8')

    OP_64(0x00, 0x0001)

    def _loc_3DC(): pass

    label('loc_3DC')

    Jump('loc_48A')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6F),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_43C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_439',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_439(): pass

    label('loc_439')

    Jump('loc_48A')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_48A(): pass

    label('loc_48A')

    OP_72(0x0003, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x000B, 0x0010)

    Jump('loc_4AC')

    def _loc_49C(): pass

    label('loc_49C')

    OP_64(0x00, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_4BC',
    )

    OP_B2(0x00, 0x03, 0x0080)

    def _loc_4BC(): pass

    label('loc_4BC')

    Return()

# id: 0x0002 offset: 0x4BD
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(-107370, 0, -940, 0)
    SetChrPos(0x0101, -107570, 0, -2230, 0)
    SetChrPos(0x0102, -108910, 0, -1630, 90)
    SetChrPos(0x0107, -107270, 0, -860, 225)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010070761V#001F哎呀～\n',
            '真没想到来的会是提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070762V而且还是那么有名的博士的孙女。\n',
            '刚才真是让我吃了一惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070763V#019F我也是啊。\n',
            '怪不得操作导力器的技术那么熟练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070764V#067F哎～嘿嘿，\n',
            '其实也没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070765V不管爷爷怎么出名也好，\n',
            '我还只是个实习生而已啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070766V#064F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070767V你们要找爷爷谈的事，\n',
            '和游击士的工作有关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070768V#007F嗯……\n',
            '算是一半有关一半无关吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070769V#509F总之就是三言两语说不完的，\n',
            '又复杂又离奇的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070770V#010F详细的情况\n',
            '还是等见到你爷爷再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070771V#560F啊，好的，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070772V#060F那个那个，\n',
            '我家就在城镇的西南面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070773V下了导力扶梯之后，\n',
            '一直向市街区的南面走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070774V#061F然后到了门口那里再向西拐就到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070775V#006F明白了。\n',
            '那么我们赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003F, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x802
@scena.Code('func_03_802')
def func_03_802():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A9, 1, 0x549))
    OP_64(0x00, 0x0001)
    OP_2B(0x0041, 0x0001)
    CameraMove(-113730, 0, 22590, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 7, 0x52F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BEB',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 7, 0x52F))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_895',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080828V#004F啊……\n',
            '约修亚，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080829V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BD')

    def _loc_895(): pass

    label('loc_895')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080830V#004F啊……\n',
            '约修亚，那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080831V#012F嗯。\n',
            '是刚才所说的发烟筒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BD')

    def _loc_8F8(): pass

    label('loc_8F8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_95F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080832V#065F啊……\n',
            '哥哥，这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080833V#012F是刚才所说的发烟筒。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BD')

    def _loc_95F(): pass

    label('loc_95F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9BD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050080834V#057F这个……\n',
            '就是那发烟筒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080835V#012F阿加特兄。\n',
            '给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9BD(): pass

    label('loc_9BD')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrPos(0x0102, -114480, 0, 21800, 45)
    SetChrPos(0x0101, -115670, 0, 21890, 90)
    SetChrPos(0x0107, -114840, 0, 20630, 45)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_A3B',
    )

    SetChrPos(0x0106, -116160, 0, 20300, 0)

    def _loc_A3B(): pass

    label('loc_A3B')

    FadeIn(600, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B16',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080836V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080837V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080838V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080839V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080840V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE8')

    def _loc_B16(): pass

    label('loc_B16')

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0101,
        (
            '#0010080841V#501F哇……\n',
            '烟雾没有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080842V#560F约修亚哥哥，\n',
            '好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080843V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080844V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080845V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE8(): pass

    label('loc_BE8')

    Jump('loc_D0A')

    def _loc_BEB(): pass

    label('loc_BEB')

    FadeOut(600, 0, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚很熟练地把发烟筒拆散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetChrPos(0x0102, -114480, 0, 21800, 45)
    SetChrPos(0x0101, -115670, 0, 21890, 90)
    SetChrPos(0x0107, -114840, 0, 20630, 45)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_C6F',
    )

    SetChrPos(0x0106, -116160, 0, 20300, 0)

    def _loc_C6F(): pass

    label('loc_C6F')

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 6, 0x53E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D0A',
    )

    SetScenaFlags(ScenaFlag(0x00A7, 6, 0x53E))

    ChrTalk(
        0x0106,
        (
            '#0050080846V#052F哦……\n',
            '还挺有两下子的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080847V#012F别的地方肯定还有\n',
            '和这个一样的发烟筒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080848V找到了就把它们拆散吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0A(): pass

    label('loc_D0A')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xD0D
@scena.Code('func_04_D0D')
def func_04_D0D():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了按钮，没有任何反应。\n',
            '导力梯好像不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0xD76
@scena.Code('func_05_D76')
def func_05_D76():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    SetScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x0006 offset: 0xD8C
@scena.Code('func_06_D8C')
def func_06_D8C():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    SetScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x0007 offset: 0xDA2
@scena.Code('func_07_DA2')
def func_07_DA2():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    SetScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x0008 offset: 0xDB8
@scena.Code('func_08_DB8')
def func_08_DB8():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xE08
@scena.Code('func_09_E08')
def func_09_E08():
    OP_13(0x0094)

    Return()

# id: 0x000A offset: 0xE0C
@scena.Code('func_0A_E0C')
def func_0A_E0C():
    OP_13(0x0093)

    Return()

# id: 0x000B offset: 0xE10
@scena.Code('func_0B_E10')
def func_0B_E10():
    OP_13(0x0096)

    Return()

# id: 0x000C offset: 0xE14
@scena.Code('func_0C_E14')
def func_0C_E14():
    OP_13(0x0095)

    Return()

# id: 0x000D offset: 0xE18
@scena.Code('func_0D_E18')
def func_0D_E18():
    OP_13(0x0098)

    Return()

# id: 0x000E offset: 0xE1C
@scena.Code('func_0E_E1C')
def func_0E_E1C():
    OP_13(0x0097)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
